.. image:: https://travis-ci.org/sirosen/git-fortune.svg?branch=master
    :alt: build status
    :target: https://travis-ci.org/sirosen/git-fortune

.. image:: https://img.shields.io/pypi/v/git-fortune.svg
    :alt: Latest Released Version
    :target: https://pypi.org/project/git-fortune

.. image:: https://img.shields.io/pypi/pyversions/git-fortune.svg
    :alt: Supported Python Versions
    :target: https://pypi.org/project/git-fortune

.. image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :alt: License
    :target: https://opensource.org/licenses/Apache-2.0


git-fortune
===========

A `fortune`-like program which shows `git` tips.

Installation
------------

Install via `pip install git-fortune`.

I recommend installing with `--user` and then adding the install location to
your PATH. For example::

    pip install --user git-fortune
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> "$HOME/.bashrc"  # or equivalent

Usage
-----

Get a random git tip::

    git-fortune

or::

    git fortune


Testing, Development, and Contributing
--------------------------------------

Go to the
`CONTRIBUTING <https://github.com/sirosen/git-fortune/blob/master/CONTRIBUTING.adoc>`_
guide for detail.

CHANGELOG
---------

Unreleased
~~~~~~~~~~

0.0.1
~~~~~

Initial version
