from setuptools import setup
from setuptools import find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


required = ['pandas>=0.25.2', 'numpy>=1.17.0', 'matplotlib>=3.0.0']

extras_required = dict()
extras_required['tests'] = ['pytest>=4.0.0', 'pytest-pep8']

setup(name='edautils',
      version='0.1.1',
      description=
      'This package contains exploratory data analysis (EDA) helper functions',
      long_description=readme,
      author='David Furrer',
      author_email='furrer.david1@gmail.com',
      url='https://github.com/davidfurrer/edautils',
      license=licence
      install_requires=required,
      extras_require=extras_required,
      packages=find_packages(exclude=('tests')),
      package_data={'edautils': ['data/*']})