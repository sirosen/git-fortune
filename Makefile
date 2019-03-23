VERSION=$(shell grep '^__version__' git_fortune/version.py | cut -d '"' -f2)

.PHONY: release localdev test clean showvars help

help:
	@echo "These are our make targets and what they do."
	@echo "All unlisted targets are internal."
	@echo ""
	@echo "  help:          Show this helptext"
	@echo "  localdev:      Setup local development env with a 'pip install -e'"
	@echo "  showvars:      Show makefile variables"
	@echo "  test:          Lint and test code"
	@echo "  autoformat:    Format code with black + isort"
	@echo "  release:       Build, tag, release to pypi"
	@echo "  clean:         Remove typically unwanted files"


showvars:
	@echo "VERSION=$(VERSION)"


.venv:
	virtualenv --python=python3 .venv
	.venv/bin/pip install -U pip setuptools twine tox
	.venv/bin/pip install -e '.[development]'
localdev: .venv

build: $(VIRTUALENV)


release: $(VIRTUALENV)/bin/twine
	rm -rf dist/
	.venv/bin/python setup.py sdist bdist_wheel
	.venv/bin/twine upload dist/*
	git tag -s "$(VERSION)" -m "v$(VERSION)"

test: .venv
	.venv/bin/tox


autoformat: .venv
	.venv/bin/isort --recursive tests/ git_fortune/ setup.py
	.venv/bin/black tests/ git_fortune/ setup.py

clean:
	rm -rf .venv
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	find . -name '*.pyc' -delete
