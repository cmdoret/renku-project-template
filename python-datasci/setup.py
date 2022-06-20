from setuptools import setup, find_packages

setup(
    name='{{ __sanitized_project_name__ | replace("-", "_")}}',
    version="0.1.0",
    packages=find_packages(),
)
