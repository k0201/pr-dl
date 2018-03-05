#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Bohdan Bobrowski

from setuptools import setup

setup(
    name='pr-dl',
    version='0.1',
    description="Polish Radio Downloader",
    url="https://github.com/bohdanbobrowski/pr-dl",
    author="Bohdan Bobrowski",
    author_email="bohdanbobrowski@gmail.com",
    license="MIT",
    packages=["pr-dl"],
    install_requires=["eyed3", "mutagen", "slugify", "pycurl", "PIL", "clint"],
    entry_points={
        'console_scripts': ['prdl=pr-dl.pr-dl-cli:main'],
    },
)
