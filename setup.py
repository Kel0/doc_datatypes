import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="doc_datatypes",
    version="0.0.6",
    author="Example Author",
    author_email="rickeyfsimple@example.com",
    description="Dict with documentation _-_",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kel0/doc_datatypes",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.7',
)