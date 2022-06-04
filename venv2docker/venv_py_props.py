import subprocess
from pathlib import Path
from typing import List, IO

from packaging.version import Version


def collect_pip_dependencies(path: Path, output_path: Path) -> List[str]:
    """
    Copy virtualenv requirements to given output path
    :param path: virtualenv base path
    :param output_path: path to contain the new requirements.txt
    :return: list of required packages
    """
    file = open(output_path / 'requirements.txt', 'w+')
    subprocess.run([path / 'Scripts' / 'pip.exe', 'freeze'], stdout=file)
    
    dependencies = _patch_subprocess_result_junk(file)

    return dependencies


def get_venv_python_version(path: Path) -> Version:
    version_bytes = (subprocess.check_output(
        [path / 'Scripts' / 'python.exe', '-c', "import platform;print(platform.python_version())"], shell=True))
    return Version(version_bytes.decode())


def _patch_subprocess_result_junk(file: IO) -> List[str]:
    """
    Patch subprocess result object bytes appearing at the last line
    """
    file.seek(0)
    lines = file.readlines()
    lines = [line for line in lines if line != '\n'][:-1]
    file.truncate(0)
    file.seek(0)
    file.writelines(lines)

    return lines
