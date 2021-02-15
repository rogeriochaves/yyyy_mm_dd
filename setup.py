from setuptools import find_packages, setup

setup(
    name='yyyy_mm_dd',
    packages=find_packages(include=['yyyy_mm_dd']),
    version='0.1.0',
    description='Helper functions for easy string-based manipulation of dates in python',
    author='Rogerio Chaves',
    url="https://github.com/rogeriochaves/yyyy_mm_dd",
    license='MIT',
    python_requires='>=3.6',
    install_requires=['python-dateutil'],
)