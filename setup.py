from setuptools import setup
from setuptools import find_packages
from os.path import abspath
from os.path import dirname
from os.path import join


here = abspath(dirname(__file__))

with open(join(here, 'pytail', 'VERSION'), encoding='utf-8') as file:
    version = file.read().strip()


setup(
    include_package_data=True,
    name='pytail',
    py_modules=['tail'],
    version=version,
    description='Unix Tail implementation',
    author='Gerald Leikam',
    author_email='gerald.leikam@aol.com',
    url='https://github.com/GeraldLeikam/py-tail',
    packages=find_packages(exclude=[]),
    package_data={
        'pytail': ['VERSION'],
    },
    long_description='Unix Tail implementation',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
