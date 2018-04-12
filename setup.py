""" A wechat Robot 
See:
https://github.com/LouisCaixuran/robot
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
import itchat

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='robot',

    version=itchat.__version__,

    description='A  wechat  Robot ',
    long_description=long_description,

    url='https://github.com/LouisCaixuran/robot',

    author='LouisCaixuran',
    author_email='louiscaixuran@163.com',

    license='MIT',

    classifiers=[
        'Development Status :: 0.1',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
    ],

    keywords=' A wechat robot ',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    install_requires=['requests', 'pyqrcode', 'pypng','itchat'],

    # List additional groups of dependencies here
    extras_require={},
)
