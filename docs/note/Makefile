NOTE_NAME=note

CERTIFICATES_DIR=/usr/share/pki/ca-trust-source/anchors
ARTIFACTORY_URL=https://artifactory.corp.kelkoo.net/api/pypi/pypi-local

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
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "${_BLUE}%-10s${_END} %s\n", $$1, $$2}'

tex: ## Process note
	tectonic ${NOTE_NAME}.tex

open: ## Open note
	evince ${NOTE_NAME}.pdf &

clean: ## Clean output
	rm -rf ${NOTE_NAME}.pdf
