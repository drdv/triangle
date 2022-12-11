PYTHON=python
VENV_NAME=.venv
PYLINT=pylint
HTML_DIR=docs/sphinx/build/html
TMP_PYLINT_FILE=.pylint_report.json

_BLUE=\033[34m
_END=\033[0m

# canned recipe
define show =
echo -e "${_BLUE}============================================================${_END}" && \
echo -e "${_BLUE}[$@] ${1}${_END}" && \
echo -e "${_BLUE}============================================================${_END}"
endef

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "${_BLUE}%-15s${_END} %s\n", $$1, $$2}'

.PHONY: docs
docs: lint test note ## Generate sphinx docs
	cd docs/sphinx && make html

pre-commit: ## Execute pre-commit on all files
	@pre-commit run -a

lint: lint-run lint-copy-to-docs ## Lint code

test: test-run test-copy-to-docs ## Run unit tests

note:
	-@cd docs/note && make tex
	mkdir -p $(HTML_DIR)
	rm -rf $(HTML_DIR)/note.pdf
	cp docs/note/note.pdf $(HTML_DIR)

lint-run:
	-@$(PYLINT) triangle/* triangle/utest/* > ${TMP_PYLINT_FILE} || exit 0
	-@pylint_report ${TMP_PYLINT_FILE} -o .pylint_report.html

lint-copy-to-docs:
	mkdir -p $(HTML_DIR)
	rm -rf $(HTML_DIR)/.pylint_report.html
	mv -f .pylint_report.html $(HTML_DIR)
	rm ${TMP_PYLINT_FILE}

test-run:
	coverage run -m pytest -v
	coverage html

test-copy-to-docs:
	mkdir -p $(HTML_DIR)
	rm -rf $(HTML_DIR)/.htmlcov
	rm -rf $(HTML_DIR)/.utest_reports
	mv -f .htmlcov $(HTML_DIR)
	mv -f .utest_reports $(HTML_DIR)
	rm -rf .coverage .pytest_cache

.PHONY: open
open: ## Open sphinx documentation
	brave-browser ${HTML_DIR}/index.html

setup-venv: ## Setup empty venv
	${PYTHON} -m venv ${VENV_NAME} && \
	. ${VENV_NAME}/bin/activate && \
	pip install --upgrade pip

install-local: setup-venv ## Editable install in venv
	. ${VENV_NAME}/bin/activate && pip install -e .[dev]

dist-local: setup-venv ## Build package
	. ${VENV_NAME}/bin/activate && pip install build && ${PYTHON} -m build

.PHONY: clean
clean: ## Clean stuff
	rm -rf docs/sphinx/build
	rm -rf docs/sphinx/source/.autosummary
	find . -name ".ipynb_checkpoints" | xargs rm -rf
	find . -name "__pycache__" | xargs rm -rf
	rm -rf *.egg-info dist .pytest_cache .coverage
	cd docs/note && make clean
