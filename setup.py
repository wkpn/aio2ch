from pathlib import Path
from setuptools import setup

import re


def get_version(package):
    data = Path(package, "__version__.py").read_text()
    version = re.findall(r"^__version__ = \"([^']+)\"\r?$", data, re.M)[0]

    return version


def get_packages(package):
    return [str(path.parent) for path in Path(package).glob("**/__init__.py")]


with open("README.rst", "r", encoding="utf-8") as readme:
    long_description = readme.read()

with open("requirements.txt", "r", encoding="utf-8") as requirements:
    install_requires = [dependency.strip('\n') for dependency in requirements]

with open("requirements-dev.txt", "r", encoding="utf-8") as requirements_dev:
    tests_require = [dependency_dev.strip("\n") for dependency_dev in requirements_dev]


setup(
    name="aio2ch",
    version=get_version("aio2ch"),
    python_requires=">=3.6",
    packages=get_packages('aio2ch'),
    package_dir={"aio2ch": "aio2ch"},
    url="https://github.com/wkpn/aio2ch",
    license="MIT",
    author="wkpn",
    description="Fully asynchronous read-only API wrapper for 2ch.hk (dvach)",
    long_description=long_description,
    install_requires=install_requires,
    tests_require=tests_require,
    keywords=["2ch", "Двач", "Dvach", "api", "wrapper", "async"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    entry_points={
        "console_scripts": [
            "aio2ch = aio2ch.cli:download",
        ]
    }
)
