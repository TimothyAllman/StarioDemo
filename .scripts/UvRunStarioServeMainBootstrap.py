import os
from pathlib import Path

from dotenv import load_dotenv
from stario.cli import main as stario_main_cli


def _repo_root(
    script_path: Path,
) -> Path:
    return script_path.resolve().parents[1]


def _read_port_from_env() -> str:

    raw_port = os.getenv(
        key="STARIODEMO_API_PORT",
        default="8000",
    )
    port = raw_port.strip().strip('"').strip("'")
    if not port.isdigit():
        raise ValueError(f"STARIODEMO_API_PORT must be an integer, got: {raw_port!r}")

    return port


def RunStario() -> int:
    root = _repo_root(Path(__file__))
    load_dotenv(
        dotenv_path=root / ".env",
        override=False,
    )
    port = _read_port_from_env()
    args = ["serve", "main:bootstrap", "--port", port]

    return stario_main_cli(args)


if __name__ == "__main__":
    raise SystemExit(RunStario())
