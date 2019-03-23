"""
A simple "database" of tips which we can identify by
- ID (number)
- Category (string)
"""

# globals (don't freak out, this is fine)
TIPS_BY_ID = {}
TIPS_BY_CATEGORY = {}


class Tip(object):
    _tipid = 0

    def __init__(self, tipstr, category="general"):
        self.tipid = Tip._tipid
        Tip._tipid += 1

        self.tipstr = tipstr.strip()

        self.category = category


def add_tip(tipstr, **kwargs):
    global TIPS_BY_ID
    global TIPS_BY_CATEGORY
    tip = Tip(tipstr, **kwargs)
    TIPS_BY_ID[tip.tipid] = tip
    if tip.category not in TIPS_BY_CATEGORY:
        TIPS_BY_CATEGORY[tip.category] = []
    TIPS_BY_CATEGORY[tip.category].append(tip)


add_tip(
    """
To see changes which are in the staging area, use `git diff --staged`
""",
    category="diff",
)


add_tip(
    """
Modify your last commit before pushing with `git commit --amend`
""",
    category="commit",
)


add_tip(
    """
Use `git commit --verbose` to show a unified diff in your editor below the
commit message you are writing. This can help you write good commit messages!
""",
    category="commit",
)


add_tip(
    """
`git log --graph` can show you a tree-like representation of the git history.

Try adding in `--oneline --decorate --all`
""",
    category="log",
)
