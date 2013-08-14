import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('haystackui/requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='haystackui',
    version='0.1',
    packages=['haystackui'],
    include_package_data=True,
    #license='BSD License',  # example license
    description='A basic wrapper around haystack making it even easier to quickly add search to your app',
    long_description=README,
    install_requires=required,
    url='https://github.com/TangentSolutions/Tangent-Haystack-UI',
    author='Christo Crampton'
)
