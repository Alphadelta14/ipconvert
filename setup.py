#!/usr/bin/env python
"""
ipconvert

vBulletin to IPBoards standalone converter

2016, AlphaServ Computing Solutions
"""

from __future__ import print_function


from setuptools import setup, find_packages


__version__ = '0.1.0'  # Overwritten below
with open('ipconvert/version.py') as handle:
    exec(handle.read())  # pylint: disable=exec-used

setup(
    name='ipconvert',
    version=__version__,
    description='vBulletin to IPBoards standalone converter',
    url='https://github.com/Alphadelta14/ipconvert',
    author='',
    author_email='',
    license='Other/Proprietary License',
    extras_require={
        "doc": [
            "sphinx>=1.3,<2",
            "sphinx_rtd_theme==0.1.9",
            "numpydoc>=0.4.0,<1.0"
        ],
        "dev": [
            "twine>=1.7.0,<1.8.0"
        ]
    },
    install_requires=[
        'mysqlclient>=1.3.7',
    ],
    packages=find_packages(),
    include_package_data=False,  # Update MANIFEST.in if changed
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
