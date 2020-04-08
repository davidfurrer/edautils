from setuptools import setup
from setuptools import find_packages

required = ['pandas', 'numpy', 'matplotlib']

extras_required = dict()
extras_required['tests'] = ['pytest>=4.0.0', 'pytest-pep8']

setup(name='edautils',
      version='0.1.0',
      description=
      'This package contains exploratory data analysis (EDA) helper functions',
      author='David Furrer',
      author_email='furrer.david1@gmail.com',
      install_requires=required,
      extras_require=extras_required,
      packages=find_packages())