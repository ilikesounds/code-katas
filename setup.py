# -*- coding-: utf-8 -*-
from setuptools import setup

setup(
    name='flight_paths',
    description='flight_paths module',
    version=0.1,
    author='Jeff Torres',
    author_email='jeffrey.n.torres@gmail.com',
    license='MIT',
    py_modules=['flight_path', 'simple_graph'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
    entry_points={}
)
