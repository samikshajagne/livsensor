from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    requirements_list: List[str] = []
    # You can add your logic to populate the requirements_list here
    return requirements_list

setup(
    name='sensor',
    version="0.0.1",
    author="Samiksha",
    author_email='samikshajagne2@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()  # ["pymongo"]
)
