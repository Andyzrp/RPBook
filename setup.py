#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if sys.version_info < (3, 7):
    print(u"The minimum support Python 3.7\n支持最低版本 3.7")
    exit(1)

import os
from setuptools import find_packages
from setuptools import setup
from RPBook import __author__, __version__

L = []
for path, dir_list, file_list in os.walk("./RPBook/assets"):
    for file_name in file_list:
        L.append(os.path.relpath(os.path.join(path, file_name), "./RPBook"))

setup(
    name='RPBook',
    version=__version__,
    description="markdown 静态网页生成器",
    long_description=open('README.md', 'r', encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author=__author__,
    author_email='1450644462@qq.com',
    url='https://github.com/Andyemmmm/RPBook',
    project_urls={
        '样板': 'https://andyemmmm.github.io/',
    },
    packages=find_packages(),
    package_data={"": L},
    # include_package_data=True,
    license="MIT",
    zip_safe=True,
    keywords='RPbook md',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    install_requires=['mistletoe', ],
    entry_points={
        'console_scripts': [
            'RPbook = RPBook.RPbook:main',
        ]
    }
)
