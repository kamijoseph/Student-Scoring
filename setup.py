
# setup
from setuptools import find_packages, setup
from typing import List

E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:
    """Return a clean list of requirements, skipping editable installs."""
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()
            if req and req != "-e .":
                requirements.append(req)
    return requirements


setup(
    name = "Students_scores",
    version = "0.0.1",
    author = "Kami",
    author_email = "josephkiarie561@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)