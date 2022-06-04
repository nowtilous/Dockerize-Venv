from distutils.core import setup

setup(
    name='venv2docker',
    packages=['venv2docker'],
    version='1.0',
    license='MIT',
    description='Convert virtual env to docker container!',
    author='McLovin',
    author_email='e.e@e.com',
    url='https://github.com/nowtilous/Dockerize-Venv',
    keywords=['docker', 'virtualenv', 'venv', 'converter'],
    install_requires=[
        'packaging',
    ],
    entry_points={
        'console_scripts': [
            'dockerize = venv2docker.dockerize:main',
            'venv2docker = venv2docker.dockerize:main',
        ],
    },
)
