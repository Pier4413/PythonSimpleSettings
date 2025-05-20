from setuptools import setup
from settings.metadata.__version__ import __version__

setup(
    name='settings',
    packages=['settings'],
    description='A simple wrapper for configparser',
    version=__version__,  # updated
    url='https://github.com/Pier4413/PythonSimpleSettings',
    author='Panda',
    author_email='panda@delmasweb.net',
    install_requires=[
        'configparser'
    ],
    keywords=['settings']
)
