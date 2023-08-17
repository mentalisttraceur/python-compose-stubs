default:
	python setup.py sdist
	python setup.py bdist_wheel

clean:
	rm -rf build *.egg-info dist
