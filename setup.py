import os

from setuptools import setup, find_packages

__version__ = '0.0.1'


requirements_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'requirements.txt')
with open(requirements_path) as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name='Project_name',
    version=__version__,
    description='Project Description',
    url='Git Hub Project URL',
    maintainer='',
    maintainer_email='',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    dependency_links=[],
    install_requires=requirements,
    extras_require={},
    python_requires=">=3.7",
    classifiers=[
        'Programming Language :: Python :: 3.7'
    ],
)
