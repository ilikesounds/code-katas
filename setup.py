# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="forbes",
    description="Implementation of the forbes youngest billionaire sorter",
    version='0.1.0',
    author="Jeff Torres",
    author_email="jeffrey.n.torres@gmail.com",
    license='MIT',
    py_modules=['forbes`'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
)
