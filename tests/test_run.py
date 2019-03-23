import subprocess


def test_help():
    subprocess.check_call(["git-fortune", "-h"])


def test_version():
    subprocess.check_call(["git-fortune", "--version"])
