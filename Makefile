all:
	python setup.py install
	python -m nltk.downloader all

check:
	python setup.py test
