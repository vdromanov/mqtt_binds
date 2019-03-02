from setuptools import setup, find_packages
from os.path import join, dirname
from mqtt_binds import __version__

setup(
    name='mqtt_binds',
    version=__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    install_requires=[
            'paho-mqtt==1.4.0'
            ]
)
