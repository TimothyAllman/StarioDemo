import subprocess
import sys

PICCOLO_APP_NAME = "WebsiteFeatureWidgetPkg"


def create_migration(app_name="all", auto=True):
    """
    Executes 'uv run piccolo migrations new' via subprocess.
    """

    # Build the base command using uv run
    command = [
        "uv",
        "run",
        "piccolo",
        "migrations",
        "new",
        app_name,
    ]

    # Append --auto flag if requested
    if auto:
        command.append("--auto")
        print(f"Generating automatic migration for app: '{app_name}'...")
    else:
        print(f"Generating blank/manual migration for app: '{app_name}'...")

    try:
        # Run the command and stream output directly to the terminal
        result = subprocess.run(command, check=True, text=True)
        print("Migration file created successfully!")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Error during migration generation: {e}", file=sys.stderr)
        sys.exit(e.returncode)
    except FileNotFoundError:
        print(
            "Error: 'uv' command not found. Ensure uv is installed and in your PATH.",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    # Default to creating an auto-migration for 'all' apps.
    # Change 'all' to a specific app name (e.g., 'my_app') if needed.
    create_migration(
        app_name=PICCOLO_APP_NAME,
        auto=True,
    )
