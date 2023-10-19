from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="AutoLibLoader",
    version="0.0.1",
    author="Volin Nilov",
    author_email="rbuswork@inbox.ru",
    description='A package allows you to automatically download the necessary libraries through the Python programming languages PIP package manager. The list of required libraries is given in the file "requirements.txt". This code is intended for fast and automatic deployment of already existing program code on a new device, automating the process of downloading the necessary libraries through the PIP package manager.',
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/VolinLab/AutoLibLoader/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10.0",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)