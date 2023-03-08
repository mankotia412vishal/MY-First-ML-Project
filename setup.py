from setuptools import find_packages, setup 
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of the requirements
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]
         
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)

    return requirments


setup(
    name='myfistmlproject',
    version='0.0.1',
    autjor='Vishal Singh',
    author_email='mankotia412vishal@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)