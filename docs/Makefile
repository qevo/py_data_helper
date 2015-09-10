# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = .

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(BUILDDIR)
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(BUILDDIR)


html:
	@old_dir=`cd .; pwd`

	@`cd $(BUILDDIR)`

	@echo "remove docs from git index"
	@git ls-files | xargs -I %s git rm --cache %s

	@echo "remove any existing files"
	@rm .buildinfo || true
	@rm *.html || true
	@rm *.inv || true
	@rm *.js || true
	@rm *.rst || true
	@rm -r doctrees || true
	@rm -r _modules || true
	@rm -r _sources || true
	@rm -r _static || true

	@echo "find *.rs_ files and copy them as *.rst (used for static files)"
	@find . -depth -name "*.rs_" -exec sh -c 'cp "$$1" "$${1%.rs_}.rst"' _ {} \; || true

	@echo "find python packages and generate API documentation"
	@find .. -depth -name "__init__.py" -exec sh -c 'sphinx-apidoc -f -T -e -o . "$${1%__init__.py}"' _ {} \; || true

	@echo "convert markdown files"
	@pandoc --from=markdown --to=rst --output=changelog.rst ../CHANGELOG.md

	@echo "generate HTML documentation"
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) .

	@echo "remove doctrees"
	@rm -r doctrees

	@echo "add docs to git index"
	@git add *

	@echo
	@echo "Build finished. The HTML page is in `cd .; pwd`."
	@`cd $$old_dir`
	@echo
