from setuptools import setup, find_packages

# Read the contents of requirements.txt and split lines into a list
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='genetic-palindrome-finder',
    version='1.0.0',
    packages=find_packages(),
    install_requires=requirements,  # Include the dependencies from requirements.txt
    entry_points={
        'console_scripts': [
            'genetic-palindrome-finder=genetic_palindrome_finder:main',
        ],
    },
)
