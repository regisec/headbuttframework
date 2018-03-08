# -*- coding: UTF-8 -*-
"""
    Created by Régis Eduardo Crestani <regis.crestani@gmail.com> on 30/06/2016.
"""
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

setup(
    name='headbutt-framework',
    version='0.0.0',
    description='Headbutt Framework',
    url='https://github.com/regisec/headbutt-framework/',
    author='Régis Eduardo Crestani',
    author_email='regis@headbutt.games',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Topic :: Software Development',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=['docs', 'test']),
    install_requires=[],
)
