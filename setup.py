# encoding: utf-8
from setuptools import setup
from version import version, name, authors, email, short_desc

def readme():
    """Import README for use as long_description."""
    with open("README.rst") as f:
        return f.read()

setup(
    name=name,
    version=version,
    description=short_desc,
    long_description=readme(),
    url="https://github.com/jplusplus/vantetider-scraper",
    author=authors,
    author_email=email,
    license="MIT",
    packages=["vantetider"],
    zip_safe=False,
    install_requires=[
        "pandas",
        "requests",
        "requests_cache"
    ],
    test_suite="nose.collector",
    tests_require=["nose"],
    include_package_data=True,
    download_url="https://github.com/jplusplus/vantetider-scraper/archive/%s.tar.gz"
                 % version,
)
