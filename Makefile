all: python c

python:
	python3 compile_python.py

c:
	python3 compile_c.py

build: python
	rm -f dist/*
	python3 setup.py sdist

upload: build
	twine upload dist/*
