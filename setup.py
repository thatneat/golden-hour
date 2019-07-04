#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="golden_hour",
    version="1.0.0",
    author="Alan Hussey",
    description="Record a sunset timelapse and post it to Twitter with a weather report",
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
