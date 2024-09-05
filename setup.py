# setup.py
from setuptools import find_packages, setup

setup(
    name="constructor-lib",
    version="0.0.1",
    author="Chris Mangum",
    author_email="csmangum@gmail.com",
    description="Constructor is a Python library that enables the simulation and exploration of physical transformations within the framework of Constructor Theory, focusing on what tasks are possible or impossible under the laws of physics.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/constructor-lib/",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
