import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="alchemize",
    version="0.0.1",
    description="Make changes to sql tables using SqlAlchmey",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/eddiethedean/alchemize",
    author="Odos Matthews",
    author_email="odosmatthews@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=['SQLAlchemy>=1.4']
)