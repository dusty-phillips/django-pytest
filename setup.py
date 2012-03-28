from setuptools import setup
from setuptools import find_packages

setup(
        name="django-pytest",
        version="0.2.0",
        author="Dusty Phillips",
        author_email="dusty@archlinux.ca",
        packages=find_packages(),
        url="http://github.com/buchuki/django-pytest",
        license="LICENSE.txt",
        description="django test runner to use py.test tests",
        long_description=open('README.md').read(),
        zip_safe=False,
)
