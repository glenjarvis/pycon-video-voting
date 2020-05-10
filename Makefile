.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help
SHELL := /bin/bash

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

DOCKER_VERSION = latest

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## Remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 github_commit_status tests

reqs: ## Update all requirements
	poetry update
	poetry export --without-hashes -f requirements.txt -o requirements.txt
	poetry export --without-hashes --dev -f requirements.txt -o requirements_dev.txt
	poetry show --tree > requirements_graph.txt

test: ## run tests quickly with the default Python
	python tests/test_github_commit_status.py

test-all: ## Run tests in all containers
	# TODO: Please help me learn to make this more DRY
	docker-compose build
	docker run --rm -it glenjarvis/github_commit_status:latest /bin/bash -c 'make intra-container-test'
	docker run --rm -it glenjarvis/github_commit_status:py-3.5.9-latest /bin/bash -c 'make intra-container-test'
	docker run --rm -it glenjarvis/github_commit_status:py-3.6.10-latest /bin/bash -c 'make intra-container-test'
	docker run --rm -it glenjarvis/github_commit_status:py-3.7.7-latest /bin/bash -c 'make intra-container-test'

tag:
	if [ -z $${VERSION+x} ]; then echo "make tag VERSION=<<version>>"; exit 1; fi
	git tag -s v$(VERSION) -m 'Release $(VERSION)'

coverage: ## check code coverage quickly with the default Python
	coverage run --source github_commit_status python tests/test_github_commit_status.py
	coverage report -m
	coverage html

git-hook:
	cp githooks/pre-commit  .git/hooks/
	echo "Git hook installed."

git-hooks: git-hook

hook-go-away:
	rm .git/hooks/pre-commit || true
	echo "Git hook is gone. You can commit now."

hooks-go-away: hook-go-away

docs: ## generate Sphinx HTML documentation, including API docs
	@echo "+ $@"
	@rm -f docs/github_commit_status.rst
	@sphinx-apidoc -o docs/ github_commit_status
	@rm -f docs/modules.rst
	@$(MAKE) -C docs clean
	@$(MAKE) -C docs html
	@$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	# TODO: Replace twine
	twine upload dist/*

dist: clean ## builds source and wheel package
	poetry build
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	poetry install
