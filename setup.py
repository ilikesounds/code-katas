# -*- coding-: utf-8 -*-
from setuptools import setup

setup(
    name='parenthetics',
    description='proper parenthetics',
    version=0.1,
    author='Jeff Torres',
    author_email='jeffrey.n.torres@gmail.com',
    license='MIT',
    py_modules=['proper_parenthetics', 'linked_list'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
    entry_points={}
)
