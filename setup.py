from os import path
from setuptools import setup, find_packages
import sys

sys.path.insert(0, 'src')

with open(path.join('.', 'README.md')) as f:
    long_description = f.read()

setup(name='Peniot',
      version='1.0',
      description='Penetration Testing Tool for IoT devices',
      long_description=long_description,
      author='Berat Cankar,Bilgehan Bingol,Ebru Celebi,Dogukan Cavdaroglu',
      url='https://senior.ceng.metu.edu.tr/2019/peniot/',
      platform='Unix',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      install_requires=['setuptools', 'pahomqtt', 'scapy', 'pyshark-legacy', 'coapthon', 'Cython', 'pygame', 'pika', 'fpdf', 'pexpect'],
      classifiers=['Programming Language :: Python :: 2.7.9']
)
