#!/usr/bin/env python3
"""Remove a local home-directory prefix from a Sideloader release binary."""

from pathlib import Path
import sys


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(f"usage: {sys.argv[0]} BINARY HOME_DIRECTORY")

    binary = Path(sys.argv[1])
    home = sys.argv[2].encode()
    if len(home) < len(b"/build"):
        raise SystemExit("home directory path is too short to sanitize")

    replacement = b"/build" + b"_" * (len(home) - len(b"/build"))
    data = binary.read_bytes()
    binary.write_bytes(data.replace(home, replacement))

    if home in binary.read_bytes():
        raise SystemExit("local home-directory path remains in binary")


if __name__ == "__main__":
    main()
