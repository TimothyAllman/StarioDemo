import os
import platform
import sqlite3
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv

# Global context placeholders for cleaner function interoperability
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent
LITESTREAM_BIN: Path = Path(__file__).resolve().parent / ("litestream.exe" if platform.system() == "Windows" else "litestream")
CONFIG_FILE: Path = PROJECT_ROOT / "litestream.yml"


def Checkpaths():
    """Initialises environment configurations and strictly verifies required variables and architecture."""
    # Force load fresh variables directly from .env file
    load_dotenv(override=True)

    print("🚀 Initialising Stario v4 Application Environment with Litestream...")

    # Strict Environment Variable Validation (No fallbacks allowed)
    db_path = os.getenv("LITESTREAM_DB_PATH")
    if not db_path:
        print("❌ Error: ENVIRONMENT VARIABLE NOT SET: 'LITESTREAM_DB_PATH'")
        print("💡 Please define 'LITESTREAM_DB_PATH' in your .env file.")
        sys.exit(1)

    replica_url = os.getenv("LITESTREAM_REPLICAS_URL")
    if not replica_url:
        print("❌ Error: ENVIRONMENT VARIABLE NOT SET: 'LITESTREAM_REPLICAS_URL'")
        print("💡 Please define 'LITESTREAM_REPLICAS_URL' in your .env file.")
        sys.exit(1)

    # Validate essential runtime entry points exist
    target_script = PROJECT_ROOT / "main.py"
    if not target_script.exists():
        print(f"❌ Error: Could not find 'main.py' at calculated path: {target_script}")
        sys.exit(1)

    if not LITESTREAM_BIN.exists():
        print(f"❌ Error: Litestream binary missing from script directory at: {LITESTREAM_BIN}")
        sys.exit(1)

    if not CONFIG_FILE.exists():
        print(f"❌ Error: Could not find 'litestream.yml' at calculated path: {CONFIG_FILE}")
        sys.exit(1)

    # Validate that the backup folder exists if using local file protocol
    if replica_url.startswith("file://"):
        folder_name = replica_url.replace("file://", "")
        backup_dir = PROJECT_ROOT / folder_name

        if not backup_dir.exists():
            print(f"❌ Error: The configured local backup directory does not exist: {backup_dir}")
            print("💡 Please create the folder manually or update your .env replica destination before running the server.")
            sys.exit(1)


def StartLitestreamRestore():
    """Checks if the database file is missing and handles auto-restoration from the replica."""
    db_file_path = os.getenv("LITESTREAM_DB_PATH")
    if not db_file_path:
        print("❌ Error: ENVIRONMENT VARIABLE NOT SET: 'LITESTREAM_DB_PATH'")
        sys.exit(1)

    db_filename = Path(db_file_path).name
    db_absolute_check = PROJECT_ROOT / db_filename

    if db_absolute_check.exists():
        print(f"💾 Local database ({db_filename}) found. Skipping restoration step.")
        return

    print(f"⚠️ Database file ({db_filename}) missing! Attempting auto-restoration from replica...")

    restore_command = [str(LITESTREAM_BIN), "restore", "-config", str(CONFIG_FILE), db_file_path]

    try:
        subprocess.run(restore_command, check=True, cwd=PROJECT_ROOT)
        print("✅ Database successfully restored from replica.")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Restoration skipped or no previous generations found (Exit code: {e.returncode}). Proceeding with a fresh database...")


def StartLitestreamReplicate():
    """Forces SQLite into WAL mode and writes an initialization transaction to trigger replication."""
    db_file_path = os.getenv("LITESTREAM_DB_PATH")
    if not db_file_path:
        print("❌ Error: ENVIRONMENT VARIABLE NOT SET: 'LITESTREAM_DB_PATH'")
        sys.exit(1)

    db_filename = Path(db_file_path).name
    db_absolute_path = PROJECT_ROOT / db_filename

    print(f"🔧 Verifying WAL mode and initial generation state for {db_filename}...")

    conn = None
    try:
        conn = sqlite3.connect(db_absolute_path)
        cursor = conn.cursor()

        # Enable Write-Ahead Logging mode (Mandatory requirement for Litestream)
        cursor.execute("PRAGMA journal_mode=WAL;")

        # Generate initial transaction frame so Litestream replicates immediately on boot
        cursor.execute("CREATE TABLE IF NOT EXISTS _litestream_init (id INTEGER PRIMARY KEY, init_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
        cursor.execute("INSERT INTO _litestream_init DEFAULT VALUES;")
        conn.commit()
        print("⚡ Database forced into WAL mode. Transaction frame written successfully.")
    except Exception as e:
        print(f"⚠️ Warning: Auto-initialization write encountered a checkpoint hurdle: {e}")
    finally:
        if conn:
            conn.close()


def StartStario():
    """Launches the combined Litestream replication process and Stario core server."""
    command = [str(LITESTREAM_BIN), "replicate", "-config", str(CONFIG_FILE), "-exec", "uv run stario serve main:bootstrap"]

    try:
        subprocess.run(command, check=True, cwd=PROJECT_ROOT)
    except KeyboardInterrupt:
        print("\n🛑 Stario dev server and Litestream stopped cleanly.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Execution crashed with exit code: {e.returncode}")


def main():
    Checkpaths()
    StartLitestreamRestore()
    StartLitestreamReplicate()
    StartStario()


if __name__ == "__main__":
    main()
