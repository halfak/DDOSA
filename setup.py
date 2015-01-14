try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name             = "Distributed Denial of Sadness Attack",
    description      = "a Python project to automate thanks for good Wikipedia edits",
    long_description = open('README.md').read(),
    author           = "Oliver Keyes",
    url              = "https=//github.com/Ironholds/DDOSA",
    download_url     = "https=//github.com/Ironholds/DDOSA/archive/master.zip",
    author_email     = "okeyes@wikimedia.org",
    license          = open('LICENSE').read(),
    version          = open('VERSION').read().strip(),
    install_requires = ["nose"],
    packages         = ["DDOSA"],
    test_suite       = 'nose.collector',
    scripts          = [],
    classifiers      = [
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python",
      "Topic :: Scientific/Engineering :: Information Analysis",
      ]
)
