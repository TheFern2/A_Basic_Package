from setuptools import setup, find_packages

setup(
    name='my_tool',
    version='0.0.1',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
)