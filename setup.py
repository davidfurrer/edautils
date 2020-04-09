from setuptools import setup
from setuptools import find_packages

LONG_DESCRIPTION = """
**edautils** is a Python package providing exploratory data analysis (EDA) helper functions. 
edautils is well suited for many different kinds of applications:
  - Visualizing distributions
  - Summarizing datasets 
"""

required = ['pandas>=0.25.2', 'numpy>=1.17.0', 'matplotlib>=3.0.0']

extras_required = dict()
extras_required['tests'] = ['pytest>=4.0.0', 'pytest-pep8']

setup(name='edautils',
      version='0.1.4',
      description='Exploratory data analysis (EDA) helper functions',
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      author='David Furrer',
      author_email='furrer.david1@gmail.com',
      url='https://github.com/davidfurrer/edautils',
      license='MIT',
      install_requires=required,
      extras_require=extras_required,
      packages=find_packages(exclude=('tests')),
      package_data={'edautils': ['data/*']})
