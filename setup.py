import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="praproses",
    version="0.0.1",
    author="Ghifari",
    author_email="ghif.99@gmail.com",
    description="repository ini digunakan untuk melakukan data cleaning pada data transportasi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mas-Ghifari/praproses",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #python_requires='>=3.6',
)