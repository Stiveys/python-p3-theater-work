from setuptools import setup, find_packages

setup(
    name="theater_work",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy<2.0",  # Pin SQLAlchemy to version less than 2.0
        "pytest",
    ],
)