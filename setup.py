#!/usr/bin/env python

from setuptools import setup


def requirements():
    with open('requirements.txt', 'r') as f:
        reqs = [line.strip() for line in f.readlines()]
    return reqs

setup(name='nltk-lsm',
      version='0.0.1',
      description='Language Style Matching, using the NLTK',
      author='Max Thayer',
      author_email='garbados@gmail.com',
      url='https://github.com/garbados/nltk-lsm',
      packages=['lib'],
      entry_points={
          'console_scripts': [
              'nltk-lsm = lib.__init__:main',
          ],
      },
      install_requires=requirements(),
      test_suite="tests"
      )
