import os
import platform
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv


def GetProjectPaths() -> tuple[Path, Path, Path]:
    """Calculates absolute paths for project root, entry scripts, and local litestream binary."""
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    target_script = project_root / "main.py"

    # Detect Windows vs Linux extension needs
    binary_name = "litestream.exe" if platform.system() == "Windows" else "litestream"
    litestream_bin = script_dir / binary_name

    return project_root, target_script, litestream_bin


def VerifyProjectStructure(target_script: Path, project_root: Path, litestream_bin: Path):
    """Ensures critical entry points and localized binaries are present before booting."""
    if not target_script.exists():
        print(f"❌ Error: Could not find 'main.py' at calculated path: {target_script}")
        sys.exit(1)

    if not litestream_bin.exists():
        print(f"❌ Error: Litestream binary missing from script directory at: {litestream_bin}")
        sys.exit(1)

    # Read the replica URL exactly how it comes from the environment
    replica_url = os.getenv("LITESTREAM_REPLICAS_URL") or os.getenv("LITESTREAM_REPLICA_URL") or ""

    # Automatically create the backup folder if utilizing local file path targets
    if replica_url.startswith("file://"):
        folder_name = replica_url.replace("file://", "")
        backup_dir = project_root / folder_name

        if not backup_dir.exists():
            print(f"📁 Local environment detected. Creating backup directory at: {backup_dir}")
            backup_dir.mkdir(parents=True, exist_ok=True)


def BuildLitestreamCommand(project_root: Path, litestream_bin: Path) -> tuple[list[str], Path]:
    """Constructs the command array needed to launch Litestream replication."""
    config_file = project_root / "litestream.yml"

    if not config_file.exists():
        print(f"❌ Error: Could not find 'litestream.yml' at calculated path: {config_file}")
        sys.exit(1)

    # By using the explicit -exec flag instead of --, we prevent Litestream
    # from confusing your application tokens with a rogue backup URL on Windows.
    command = [str(litestream_bin), "replicate", "-config", str(config_file), "-exec", "uv run stario serve main:bootstrap"]

    return command, config_file


def HandleDatabaseRestoration(project_root: Path, config_file: Path, litestream_bin: Path):
    """Checks if the configured database file exists, falling back to a string-matched restore sequence."""
    # Pull path directly from environment to guarantee a perfect literal match with litestream.yml
    db_file_path = os.getenv("LITESTREAM_DB_PATH", "./piccolochat.db")

    # Strip down formatting to locate the file on local storage safely
    db_filename = Path(db_file_path).name
    db_absolute_check = project_root / db_filename

    if db_absolute_check.exists():
        print(f"💾 Local database ({db_filename}) found. Skipping restoration step.")
        return

    print(f"⚠️ Database file ({db_filename}) missing! Attempting auto-restoration from replica...")

    # Flags (-config) MUST be strictly placed BEFORE the db path string argument
    restore_command = [str(litestream_bin), "restore", "-config", str(config_file), db_file_path]

    try:
        subprocess.run(restore_command, check=True, cwd=project_root)
        print("✅ Database successfully restored from replica.")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Restoration skipped or no previous generations found (Exit code: {e.returncode}). Proceeding with a fresh database...")


def ExecuteApplicationProcess(command: list[str], working_dir: Path):
    """Executes the final subprocess command bundle inside the specified working directory."""
    try:
        subprocess.run(command, check=True, cwd=working_dir)
    except KeyboardInterrupt:
        print("\n🛑 Stario dev server and Litestream stopped cleanly.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Execution crashed with exit code: {e.returncode}")


def main():
    # 1. Force load fresh environment file parameters overriding standard shell cache
    load_dotenv(override=True)

    print("🚀 Initialising Stario v4 Application Environment with Litestream...")

    # 2. Locate the project paths and localized engine binaries
    project_root, target_script, litestream_bin = GetProjectPaths()

    # 3. Validate filesystem architecture and verify embedded binary presence
    VerifyProjectStructure(target_script, project_root, litestream_bin)

    # 4. Generate execution arguments using system paths
    command, config_file = BuildLitestreamCommand(project_root, litestream_bin)

    # 5. Handle database check/restore using matched relative string literal
    HandleDatabaseRestoration(project_root, config_file, litestream_bin)

    # 6. Boot up the unified application process
    ExecuteApplicationProcess(command, working_dir=project_root)


if __name__ == "__main__":
    main()
