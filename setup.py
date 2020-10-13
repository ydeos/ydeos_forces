#!/usr/bin/env python
# coding: utf-8

r"""ydeos_forces's setup.py."""

from distutils.core import setup

import ydeos_forces


setup(name=ydeos_forces.__project_name__,
      version=ydeos_forces.__version__,
      description=ydeos_forces.__description__,
      long_description='Forces model, including a Force and a SystemOfForces',
      url=ydeos_forces.__url__,
      download_url=ydeos_forces.__download_url__,
      author=ydeos_forces.__author__,
      author_email=ydeos_forces.__author_email__,
      license=ydeos_forces.__license__,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.7'],
      keywords='force forces',
      packages=['ydeos_forces'])
