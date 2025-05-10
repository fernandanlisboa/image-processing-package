from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name='image_processor_fernanda',
    version='0.0.2',
    author="Fernanda Lisboa",
    author_email="fernandavnlisboa@gmail.com",
    description="A package for processing images",
    long_description_content_type="text/markdown",
    url="https://github.com/fernandanlisboa/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)