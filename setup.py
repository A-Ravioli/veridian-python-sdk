from setuptools import setup, find_packages

setup(
    name="veridian",
    version="0.1.1",
    description="A simple SDK to clean tabular data using the Veridian API.",
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
