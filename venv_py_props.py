import subprocess
from pathlib import Path
from typing import List

from packaging.version import Version


def collect_pip_dependencies(path: Path, output_path: Path) -> List[str]:
    file = open(output_path / 'requirements.txt', 'w+')
    dep = subprocess.check_output([path / 'Scripts' / 'pip.exe', 'freeze'])
    file.write(dep.decode())

    file.seek(0)
    lines = file.readlines()
    lines = [line for line in lines if line != '\n'][:-1]
    file.truncate(0)
    file.seek(0)
    file.writelines(lines)

    return lines


def get_venv_python_version(path: Path) -> Version:
    version_bytes = (subprocess.check_output(
        [path / 'Scripts' / 'python.exe', '-c', "import platform;print(platform.python_version())"], shell=True))
    return Version(version_bytes.decode())
