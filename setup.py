import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RC_Functools",
    version="0.0.6",
    author="Sorrowful T-Rex",
    author_email="yc4120@ic.ac.uk",
    description="Extended functional tools and None-handling for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sorrowfulT-Rex/Python-Functools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
