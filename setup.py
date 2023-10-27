from setuptools import setup, find_packages

setup(
    name="cal_hack",
    version="0.0.1",
    description="cal_hack llm Postman project",
    author="Cal_hack team",
    author_email="liyufeng@berkeley.edu",
    license="Apache License, Version 2.0",
    packages=find_packages(exclude=("tests",)),
    python_requires='>=3.8',
    include_package_data=True,
    install_requires = open('requirements.txt').readlines(),
)
