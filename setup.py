from setuptools import setup, find_packages
import os


# Read the contents of the README file
def read_long_description():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()


setup(
    name="veridian",
    version="0.1.2",  # Updated version number
    description="A simple SDK to clean tabular data using the Veridian API.",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    author="Arav Kumar",
    author_email="veridiandata@gmail.com",
    url="https://github.com/A-Ravioli/veridian-api-python-sdk",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
