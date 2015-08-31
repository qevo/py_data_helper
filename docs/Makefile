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
	@echo "remove any existing files"
	@rm .buildinfo || true
	@rm $(BUILDDIR)/*.html || true
	@rm $(BUILDDIR)/*.inv || true
	@rm $(BUILDDIR)/*.js || true
	@rm $(BUILDDIR)/*.rst || true
	@rm -r $(BUILDDIR)/doctrees || true
	@rm -r $(BUILDDIR)/_modules || true
	@rm -r $(BUILDDIR)/_sources || true
	@rm -r $(BUILDDIR)/_static || true

	@echo "find *.rs_ files and copy them as *.rst (used for static files)"
	@find $(BUILDDIR) -depth -name "*.rs_" -exec sh -c 'cp "$$1" "$${1%.rs_}.rst"' _ {} \; || true

	@echo "find python packages and generate API documentation"
	@find $(BUILDDIR)/.. -depth -name "__init__.py" -exec sh -c 'sphinx-apidoc -T -e -o $(BUILDDIR) "$${1%__init__.py}"' _ {} \; || true

	@echo "generate HTML documentation"
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)

	@echo "remove doctrees"
	@rm -r $(BUILDDIR)/doctrees
	@echo
	@echo
	@old_dir=`cd .; pwd`
	@echo "Build finished. The HTML page is in `cd $(BUILDDIR); pwd`."
	@`cd $$old_dir`
