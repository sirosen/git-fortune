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
To see changes which are in the staging area, use `git diff --staged`.
""",
    category="diff",
)


add_tip(
    """
Modify your last commit before pushing with `git commit --amend`.
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

Try adding in `--oneline --decorate --all`.
""",
    category="log",
)


add_tip(
    """
When resolving a difficult merge conflict, consider using both
`git checkout --ours` and `git checkout --theirs` and copying the versions of
the conflicting files into ours/ and theirs/ directories.

This will let you easily diff and methodically work through conflicts,
file-by-file.
""",
    category="merges",
)


add_tip(
    """
Remember that `git pull` is just a `git fetch` followed by a `git merge`.
You can always run these commands yourself
""",
    category="pull",
)


add_tip(
    """
Avoid unnecessary merge commits when you `pull` by using `git pull --rebase`.

This replaces the `git merge` with a `git rebase`.
""",
    category="pull",
)


add_tip(
    """
git branches are pointers to commits. Only the commits have ancestors and
descendants -- the branches can move around (and not just forward!)
"""
)


add_tip(
    """
Use `git add --patch` to stage your changes in chunks instead of whole files.

This can also help you review your own work before committing.
""",
    category="commit",
)


add_tip(
    """
Want to only commit part of a file? Use `git add --patch` to choose which parts
you want to stage for commit.
""",
    category="commit",
)


add_tip(
    """
Want to only commit part of a file? Use `git add --patch` to choose which parts
you want to stage for commit.
""",
    category="commit",
)


add_tip(
    """
`git branch --merged` shows you a list of all branches which are merged into
HEAD. It's great for cleanup.
""",
    category="merges",
)


add_tip(
    """
Wondering if that refactor really did result in fewer lines of code?
Try `git diff --stat`.
""",
    category="diff",
)


add_tip(
    """
Just like `diff`, `git diff` takes `-w` to ignore whitespace changes.
""",
    category="diff",
)


add_tip(
    """
Do you ever accidentally push to a shared repo just because it's named
"origin"?

Rename "origin" to "upstream" with `git remote rename origin upstream` and
you'll probably stop making that mistake.
""",
    category="remotes",
)


add_tip(
    """
Set up `git tree` by running
`git config --global alias.tree 'log --graph --decorate --all'`

This puts `tree` into your ~/.gitconfig so that you can invoke `git tree` in
any repo.
""",
    category="log",
)


add_tip(
    """
Can't remember how you setup remotes in a repo? Use `git remote -v`.
""",
    category="remotes",
)
