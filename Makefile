PROFILE=~/.bashrc

all: build install

build:
	pip install -r requirements.txt
	python -m nltk.downloader all

install:
	alias nltk-lsm="python $PWD/main.py"
	echo "alias nltk-lsm=\"python $PWD/main.py\"" >> ${PROFILE}

check:
	python setup.py test