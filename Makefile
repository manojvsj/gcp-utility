
twine:
	pip install twine
	python setup.py bdist_wheel
	twine upload dist/* --verbose
	rm -rf dist
clean:
	rm -rf dist
	rm -rf gcp_utility.egg-info
	rm -rf build
