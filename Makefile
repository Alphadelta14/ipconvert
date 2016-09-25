
docs:
	cd {docs_dir} && sphinx-build -b html $(SPHINXOPTS) -d _build/doctrees . _build/html
	
