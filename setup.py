from setuptools import find_packages,setup
from typing import List

hypen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path,'r') as f:
        requirements=f.readlines()
        requirements = [req.replace('\n','') for req in requirements if req !='-e .']

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
name='Credit Risk Prediction',
version='0.0.1',
author='Roshan Salunke',
author_email='roshansalunke91@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)