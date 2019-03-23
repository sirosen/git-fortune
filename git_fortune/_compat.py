"""
py2 compatibility
"""

import argparse
import sys


class VersionAction(argparse.Action):
    """
    Backport of the python3 implementation (and black'ed to pass our linting)

    On python2, action="version" prints to stderr, but on python3 it prints to
    stdout. Messes up testing.
    """

    def __init__(
        self,
        option_strings,
        version=None,
        dest=argparse.SUPPRESS,
        default=argparse.SUPPRESS,
        help="show program's version number and exit",
    ):
        super(VersionAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            default=default,
            nargs=0,
            help=help,
        )
        self.version = version

    def __call__(self, parser, namespace, values, option_string=None):
        version = self.version
        if version is None:  # pragma: no cover
            version = parser.version
        formatter = parser._get_formatter()
        formatter.add_text(version)

        parser._print_message(formatter.format_help(), sys.stdout)
        parser.exit()
