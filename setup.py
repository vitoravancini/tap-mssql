#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-mssql",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_mssql"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
        "jsonref"
    ],
    entry_points="""
    [console_scripts]
    tap-mssql=tap_mssql:main
    """,
    packages=["tap_mssql"],
    package_data={'tap_mssql': [
        'tap-mssql/*.clj', 
        'tap-mssql/*/*.clj', 
        'tap-mssql/*/*/*.clj',
        'tap-mssql/*/*/*/*.clj',
        'tap-mssql/resources/log4j.properties'
    ]},
    include_package_data=True
)