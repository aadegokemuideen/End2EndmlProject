from setuptools import find_packages, setup
from typing import List

'''

setup(
    name="mlproject",
    version="0.0.1",
    author="Adegoke Muideen",
    author_email="aadegokemuideen@yahoo.com",
    packages=find_packages(),
    install_requires = [
    "pandas", 
    "numpy",
    "seaborn"
    ]
)

'''

HYPEN_E_DOT = '-e .'
def  get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requiremnts

    """
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements =[req.replace('\n',"") for req in requirements if req != HYPEN_E_DOT]

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Adegoke Muideen",
    author_email="aadegokemuideen@yahoo.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt") ##  return list of requirements
)
