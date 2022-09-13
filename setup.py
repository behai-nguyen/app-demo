"""Installation script for flask_restx demo project."""
from pathlib import Path
from setuptools import setup, find_packages

setup(
    name='dsm-python-demo',
    description='flask dev server on Synology DSM demo.',
    version='1.0.0',
    author='Van Be Hai Nguyen',
    author_email='behai_nguyen@hotmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires='>=3.9',
    install_requires=[
        'Flask',
        'python-dotenv',
        'pytest',
        'coverage',
        'simplejson',
    ],
)