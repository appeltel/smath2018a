import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smath2018a",
    version="0.0.1",
    author="Eric Appelt",
    author_email="eric.appelt@gmail.com",
    description="serious math",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/appeltel/smath2018a",
    packages=setuptools.find_packages(exclude=('tests',)),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': ['fib=smath2018a.fib:fib_cli'],
    },
)