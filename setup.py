# -*- coding: utf-8 -*-
"""
Validino is a simple validation framework with a functional
syntax.
"""
from setuptools import setup


setup(
    name='validino',
    version='0.3',
    license='MIT',
    author='Jacob Smullyan',
    author_email='jsmullyan@gmail.com',
    url='https://github.com/bwhmather/validino',
    description='A simple validation framework',
    long_description=__doc__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    platforms='OS Independent',
    packages=[
        'validino',
        ],
    include_package_data=True,
    test_suite='nose.collector',
    )
