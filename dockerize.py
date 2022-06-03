import argparse
from pathlib import Path

from venv_py_props import get_venv_python_version


def main():
    args = parse_args()
    venv_path = Path(args.path)

    if not venv_path.is_dir():
        raise NotADirectoryError("Given path is invalid")

    venv_py_version = get_venv_python_version(venv_path)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='Path to venv root')
    return parser.parse_args()


if __name__ == "__main__":
    main()
