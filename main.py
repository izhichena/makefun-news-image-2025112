#!/usr/bin/env python3
"""Copy entry.png to /output/entry.png deterministically."""
import os
import shutil
from pathlib import Path


def main() -> None:
    os.umask(0o022)
    src = Path(__file__).resolve().parent / "entry.png"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    # Permission fix: source entry.png is 0600, so a plain copy would leave the output unreadable to other users (e.g. reviewers); force 0644.
    os.chmod(dst, 0o644)


if __name__ == "__main__":
    main()
