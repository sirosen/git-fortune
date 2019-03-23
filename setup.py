import os

from setuptools import find_packages, setup

# single source of truth for package version
version_ns = {}
with open(os.path.join("git_fortune", "version.py")) as f:
    exec(f.read(), version_ns)
version = version_ns["__version__"]

setup(
    name="git-fortune",
    version=version,
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        # intentionally and explicitly left empty
    ],
    extras_require={
        # the development extra is for git-fortune developers
        "development": [
            # testing
            "pytest>=4.3.1,<5",
            # linting
            "flake8>=3.7.7,<4.0",
            "isort>=4.3.15,<5.0",
            # black requires py3.6+
            'black==19.3b;python_version>="3.6"',
            # flake-bugbear requires py3.5+
            'flake8-bugbear==18.8.0;python_version>="3.5"',
            # mock on py2, py3.4 and py3.5
            # not just py2: py3 versions of mock don't all have the same
            # interface!
            'mock==2.0.0;python_version<"3.6"',
        ]
    },
    entry_points={"console_scripts": ["git-fortune = git_fortune:main"]},
    # descriptive info, non-critical
    description="fortune-like git tips",
    long_description=open("README.rst").read(),
    author="Stephen Rosen",
    author_email="sirosen@uchicago.edu",
    url="https://github.com/sirosen/git-fortune",
    keywords=["fortune", "git"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
