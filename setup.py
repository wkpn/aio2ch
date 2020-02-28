from aio2ch import __author__, __license__, __url__, __version__

from setuptools import setup


with open('README.rst', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

with open('requirements.txt', 'r', encoding='utf-8') as requirements:
    install_requires = [dependency.strip('\n') for dependency in requirements]

with open('requirements-dev.txt', 'r', encoding='utf-8') as requirements_dev:
    tests_require = [dependency_dev.strip('\n') for dependency_dev in requirements_dev]


setup(
    name='aio2ch',
    version=__version__,
    python_requires='>=3.6',
    packages=['aio2ch'],
    package_dir={'aio2ch': 'aio2ch'},
    url=__url__,
    license=__license__,
    author=__author__,
    description='Fully asynchronous read-only API wrapper for 2ch.hk (dvach)',
    long_description=long_description,
    install_requires=install_requires,
    tests_require=tests_require,
    keywords=['2ch', 'Двач', 'Dvach', 'api', 'wrapper', 'async'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
