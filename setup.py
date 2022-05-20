from setuptools import setup, find_packages

# put the contents of your README file into the long_description
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.rst").read_text()

setup(
    long_description=long_description
)

# installation entry point used to install the new package, generate distribution files and more
# the details here will be used in the PKG-INFO file that will be generated which will contain metadata about the package
# note - the long_description argument will hold the full content of the README.rst file that was created 