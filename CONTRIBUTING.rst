Contributing to git-fortune
===========================

First off, thank you so much for taking the time to contribute! :+1:

Guidelines:

  - All code is autoformatted with `black <https://github.com/ambv/black>`_ and
     `isort <https://github.com/timothycrosley/isort>`_. You may run
      `make autoformat` to do this or configure these tools for use in your
      editor.
  - All code must pass `make test`, which runs linting and tests.
  - Use no dependencies -- git-fortune should be written in pure stdlib python
  - Yes, keep the code python2 compatible, even though python2 will soon be EOL

NOTE: `black` requires python3.6+, but the code does not

Expectations for Pull Requests
------------------------------

  - *Make sure it merges cleanly*
  - *List any issues closed by the pull request*
  - *Squash intermediate and fixup commits*

Guidelines for good commit messages:

  - No lines over 72 characters
  - No GitHub emoji -- use your words
  - Reference issues and pull requests where appropriate
  - Present tense and imperative mood
