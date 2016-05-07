# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pythaiwordcut',
    version='0.0.6',
    description='Simple Thai Wordcut in Python using Maximum Matching',
    long_description=readme,
    author='Narongdej Sarnsuwan',
    author_email='narongdej@sarnsuwan.com',
    url='https://github.com/zenyai/pythaiwordcut',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={
      'pythaiwordcut.data': ['*.db'],
   },
   include_package_data=True
)
