from setuptools import find_packages, setup
from typing import List

MINUS_E = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requiremnets
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if MINUS_E in requirements:
            requirements.remove(MINUS_E)

    return requirements


setup(
    name = 'ResumeOptimizer',
    version = '0.0.1',
    author = 'AviralWalia',
    author_email = 'aviralwalia8@gmail.com',
    packages= find_packages(),
    install_requirements = get_requirements('requirements.txt')
)