# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os, sys

with open('README.md') as f:
    readme = f.read()


setup(
    name='pythaiwordcut',
    version='0.0.9',
    description='Simple Thai Wordcut in Python using Maximum Matching',
    long_description=readme,
    author='Narongdej Sarnsuwan',
    author_email='narongdej@sarnsuwan.com',
    url='https://github.com/zenyai/pythaiwordcut',
    license="MIT",
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={
      '': ['*.db']
   },
   zip_safe=False,
   include_package_data=True
)
