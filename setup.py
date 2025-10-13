
# setup
from setuptools import find_packages, setup
from typing import List

E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    # returns a list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [requirement.replace("\n","") for requirement in requirements]

        if E_DOT in requirements:
            requirements.remove(E_DOT)
        
    return requirements

setup(
    name = "Students Scores",
    version = "0.0.1",
    author = "Kami",
    author_email = "josephkiarie561@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirement.txt")
)