import subprocess
import sys
from pathlib import Path


def main():
    print("🚀 Initialising Stario v4 Application Environment...")

    # Calculate absolute path to stariodemo/ root folder by moving 2 levels up from this script
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    target_script = project_root / "main.py"

    # Verify main.py exists at the root relative to this script
    if not target_script.exists():
        print(f"❌ Error: Could not find 'main.py' at calculated path: {target_script}")
        sys.exit(1)

    # Clean argument list for subprocess execution
    command = ["uv", "run", "stario", "serve", "main:bootstrap"]

    try:
        # cwd=project_root forces 'uv run' to execute inside stariodemo/ instead of .scripts/
        subprocess.run(command, check=True, cwd=project_root)
    except KeyboardInterrupt:
        print("\n🛑 Stario dev server stopped cleanly.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Server crashed with exit code: {e.returncode}")


if __name__ == "__main__":
    main()
