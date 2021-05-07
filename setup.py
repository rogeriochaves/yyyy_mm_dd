from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='yyyy_mm_dd',
    packages=find_packages(include=['yyyy_mm_dd']),
    version='0.1.2',
    description='Helper functions for easy string-based manipulation of dates in python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Rogerio Chaves',
    url="https://github.com/rogeriochaves/yyyy_mm_dd",
    license='MIT',
    python_requires='>=3.6',
    install_requires=['python-dateutil'],
)
