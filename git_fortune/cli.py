"""\
A fortune-like command for showing git tips

Invoke it as 'git-fortune' or 'git fortune'
"""

import argparse
import random

from . import _compat
from .database import TIPS_BY_CATEGORY, TIPS_BY_ID
from .formatter import ALL_FORMATTERS
from .version import __version__


def rand_tip(tipcollection):
    return random.choice(list(tipcollection))


def get_tip(args):
    if args.id:
        return TIPS_BY_ID[args.id]
    elif args.category:
        return rand_tip(TIPS_BY_CATEGORY[args.category])
    else:
        return rand_tip(TIPS_BY_ID.values())


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--version",
        action=_compat.VersionAction,
        version="%(prog)s " + str(__version__),
    )
    parser.add_argument(
        "--format",
        type=str.lower,
        choices=ALL_FORMATTERS.keys(),
        default="box",
        help="style of the output for tips (default: box)",
    )
    selectgroup = parser.add_mutually_exclusive_group()
    selectgroup.add_argument(
        "--category",
        choices=list(TIPS_BY_CATEGORY.keys()),
        help="the category of tips to choose from; by default choose from all tips",
    )
    selectgroup.add_argument(
        "--id", type=int, choices=list(TIPS_BY_ID.keys()), help=argparse.SUPPRESS
    )
    args = parser.parse_args()

    formatter = ALL_FORMATTERS[args.format]()
    tip = get_tip(args)
    formatter.render(tip)
