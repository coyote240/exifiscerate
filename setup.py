from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='exifiscerate',
      version='0.1',
      description='',
      long_description=long_description,
      author='Adam A.G. Shamblin',
      author_email='adam.shamblin@zeroecks.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'pelican>=4'
      ])
