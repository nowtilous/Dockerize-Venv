import configparser

from pathlib import Path
from packaging.version import Version


def get_venv_python_version(path: Path) -> Version:
    """
    Extract given venv's python version.
    :param path: path to venv root folder
    :return: Version object containing major and minor
    """
    section_stub_name = 'section_stub'
    with open(path / "pyvenv.cfg", 'r') as f:
        # Patch for venv cfg file missing section headers
        config_string = '[' + section_stub_name + ']\n' + f.read()

    config = configparser.ConfigParser()
    config.read_string(config_string)
    major, minor, *_ = config.get(section_stub_name, 'version_info').split(".")

    return Version(major + "." + minor)
