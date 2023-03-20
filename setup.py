from setuptools import setup
from setuptools import find_packages

setup(
    include_package_data=True,
    name='pytail',
    version='0.1.0',
    description='Unix Tail implementation',
    author='Gerald Leikam',
    author_email='gerald.leikam@aol.com',
    url='https://github.com/GeraldLeikam/py-tail',
    packages=find_packages(),
    long_description='Unix Tail implementation',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
