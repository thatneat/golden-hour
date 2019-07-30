#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="golden_hour",
    version="1.0.0",
    description="Record a sunset timelapse and post it to Twitter with a weather report",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alanhussey/golden-hour",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "golden-hour=golden_hour.main:main",
            "golden-hour-tweet=golden_hour.tweet:main"
        ]
    },
    install_requires=[
        "astral==1.3.4",
        "darkskylib==0.3.6",
        "python-twitter==3.4.1",
        "pytz==2016.10",
        "PyYAML==3.12",
        "schema",
        "six==1.10.0",
    ],
    include_package_data=True,
)
