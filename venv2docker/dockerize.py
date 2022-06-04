import argparse
import os
import shutil
from pathlib import Path

from venv2docker.venv_py_props import get_venv_python_version, collect_pip_dependencies


def main():
    args = parse_args()
    if not os.path.isdir(args.path):
        raise NotADirectoryError("Given path is invalid")
    venv_path = Path(args.path)
    output_path = venv_path / 'docker'
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    venv_py_version = get_venv_python_version(venv_path)
    dependencies = collect_pip_dependencies(venv_path, output_path)
    pip_ini = venv_path / 'pip.ini'
    if pip_ini.exists():
        shutil.copyfile(pip_ini, output_path / 'pip.ini')
    else:
        open(output_path / 'pip.ini', 'w+')

    print("Python version: {}\nDependencies:".format(venv_py_version))
    print(*dependencies, sep='')

    with open(output_path / 'dockerfile', 'w') as dockerfile:
        dockerfile.write("""FROM python:{version}\n\n"""
                         """COPY requirements.txt requirements.txt\n"""
                         """COPY pip.ini pip.ini\n\n"""
                         """RUN pip install -r requirements.txt""".format(version=venv_py_version))

    print("""Docker file created! now build with 'docker build --tag your_image_name {}'\n"""
          """And then 'docker run -it your_image_name /bin/bash'""".format(output_path))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='Path to venv root')
    return parser.parse_args()


if __name__ == "__main__":
    main()
