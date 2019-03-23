import argparse

from .version import __version__


def main():
    parser = argparse.ArgumentParser(
        description="fortune-like command for showing git tips"
    )
    parser.add_argument(
        "--version", action="version", version="%(prog)s " + str(__version__)
    )
    args = parser.parse_args()
    assert args  # TODO: really do stuff
