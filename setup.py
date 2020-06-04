
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-shuulaces", # the name that you will install via pip
    version="1.1",
    author="Jacob Desselles",
    author_email="jacob.desselles@gmail.com",
    description="NaN identifier and date separater",
    long_description='Will only scan NaNs if string, will also separate any date time objects into three different columns. To call functions, use isitnan(df) and splitdate(df).',
    long_description_content_type='text/markdown',# required if using a md file for long desc
    license="Apache",
    url="https://github.com/jacob-desselles/jacob_lambdata",
    #keywords="",
    packages=find_packages() # ["jacob_lambdata"]
)