APP_VERSION	:= $(shell python -c "from pygl2d import __version__; print __version__")

sdist:
	python setup.py sdist
	
upload:
	python setup.py sdist upload

install:
	python setup.py install
	
tag:
	git tag v$(APP_VERSION) -m "v$(APP_VERSION)"
	git push origin v$(APP_VERSION)
	
clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -rf `find . -name "*.pyc"`
	rm -rf `find . -name "*.pyo"`