__author__ = 'rabbiabram@gmail.com'
from setuptools import setup, find_packages
from os.path import join, dirname
PACKAGE = "pylorempyipsum"
NAME = "PyLoremPyIpsum"
DESCRIPTION = "Yet another lorem ipsum generator"
AUTHOR = "Rabbiabram"
AUTHOR_EMAIL = "rabbiabram@gmail.com"
URL = "https://github.com/rabbiabram-develop/pylorem-pyipsum"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    )