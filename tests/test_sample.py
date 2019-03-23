import random
import subprocess

import pytest

from git_fortune._compat import fix_line_endings
from git_fortune.database import TIPS_BY_ID


@pytest.mark.parametrize("tipid,tipobj", random.sample(list(TIPS_BY_ID.items()), 10))
def test_tips_boxformat(tipid, tipobj, capfd):
    subprocess.check_call(["git-fortune", "--id", str(tipid)])
    tip_lines = tipobj.tipstr.split("\n")
    captured = capfd.readouterr()
    for line in tip_lines:
        assert line in captured.out


@pytest.mark.parametrize("tipid,tipobj", random.sample(list(TIPS_BY_ID.items()), 10))
def test_tips_plainformat(tipid, tipobj, capfd):
    subprocess.check_call(["git-fortune", "--format", "plain", "--id", str(tipid)])
    captured = capfd.readouterr()
    assert fix_line_endings(tipobj.tipstr + "\n") == captured.out
