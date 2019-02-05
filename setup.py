from setuptools import setup, find_packages

setup(name='dsproject', version='1.0', packages=find_packages(),
	install_requires=[
        'requests>=2.20.0,<3'
    ],)
