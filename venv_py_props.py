import subprocess
from pathlib import Path

from packaging.version import Version


def collect_pip_dependencies(path: Path) -> str:
    return subprocess.check_output([path / 'Scripts' / 'pip.exe', 'freeze'], shell=True).decode()


def get_venv_python_version(path: Path) -> Version:
    ver_string = (subprocess.check_output(
        [path / 'Scripts' / 'python.exe', '-c', "import platform;print(platform.python_version())"], shell=True))
    return Version(ver_string.decode())
