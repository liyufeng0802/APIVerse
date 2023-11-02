from setuptools import setup, find_packages

setup(
    name="APIVerse",
    version="0.0.1",
    description="Cal Hacks 10.0 Project",
    author="Jingchao (Perry) Zhong, Jiaxiang (Calvin) Li, Junyi (Alex) Zhang, Yufeng (Jimmy) Li",
    author_email="",
    license="Apache License, Version 2.0",
    packages=find_packages(exclude=("tests",)),
    python_requires='>=3.8',
    include_package_data=True,
    install_requires = open('requirements.txt').readlines(),
)
