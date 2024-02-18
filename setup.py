import setuptools
from setuptools import find_packages
from typing import List
from setuptools import setup

Hypen_E_Dot = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    this function returns the requirements list
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
    return requirements

setup(
    Name="ML Project",
    Repo_name = "Text-Summarizer-Project"
    Src_Repo = "Text Summarizer"
    Version="0.0.1",
    author="Pavan Sai",
    author_name="pavansai24716@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)