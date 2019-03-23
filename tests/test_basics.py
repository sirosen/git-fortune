import subprocess

from git_fortune._compat import fix_line_endings
from git_fortune.version import __version__


def test_help(capfd):
    subprocess.check_call(["git-fortune", "-h"])
    captured = capfd.readouterr()
    assert (
        fix_line_endings(
            """
A fortune-like command for showing git tips

Invoke it as 'git-fortune' or 'git fortune'
"""
        )
        in captured.out
    )


def test_version(capfd):
    subprocess.check_call(["git-fortune", "--version"])
    captured = capfd.readouterr()
    assert "git-fortune {}".format(__version__) in captured.out


def test_tip_boxformat(capfd):
    subprocess.check_call(["git-fortune", "--id", "3"])
    tip3boxbody = fix_line_endings(
        """\
+-------------------------------------------------------------------------------+
| TIP #3                                                                        |
|                                                                               |
| `git log --graph` can show you a tree-like representation of the git history. |
|                                                                               |
| Try adding in `--oneline --decorate --all`.                                   |
|                                                                               |
+-------------------------------------------------------------------------------+
"""
    )
    captured = capfd.readouterr()
    assert captured.out == tip3boxbody


def test_tip_plainformat(capfd):
    subprocess.check_call(["git-fortune", "--format", "plain", "--id", "1"])
    tip1plainbody = fix_line_endings(
        "Modify your last commit before pushing with `git commit --amend`.\n"
    )
    captured = capfd.readouterr()
    assert captured.out == tip1plainbody


def test_noargs(capfd):
    """just make sure it doesn't crashfail"""
    subprocess.check_call(["git-fortune"])
    captured = capfd.readouterr()
    assert "TIP #" in captured.out  # from the box format


def test_category(capfd):
    """just make sure it doesn't crashfail"""
    subprocess.check_call(["git-fortune", "--category", "diff"])
    captured = capfd.readouterr()
    assert "TIP #" in captured.out  # from the box format


def test_category_and_id_mutex(capfd):
    ret = subprocess.call(["git-fortune", "--category", "diff", "--id", "3"])
    assert ret == 2
    captured = capfd.readouterr()
    assert "" == captured.out
    assert "argument --id: not allowed with argument --category" in captured.err
