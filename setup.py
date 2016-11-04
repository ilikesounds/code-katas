# -*- coding-: utf-8 -*-
from setuptools import setup

setup(
    name='autocomplete',
    description='autocomplete module',
    version=0.1,
    author='Jeff Torres',
    author_email='jeffrey.n.torres@gmail.com',
    license='MIT',
    py_modules=['autocomplet', 'trie'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
    entry_points={}
)
