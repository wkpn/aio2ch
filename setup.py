from aio2ch import __author__, __version__, __license__, __url__

from setuptools import setup


with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()

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
    install_requires=[
        'httpx==0.11.1',
        'aiofiles'
    ],
    tests_require=[
        'pytest',
        'pytest-asyncio',
        'pytest-cov'
    ],
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
