UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
        CCFLAGS = LINUX
	PG ?= sudo -u postgres
	INSTALL ?= sudo apt-get install 
endif
ifeq ($(UNAME_S),Darwin)
        CCFLAGS = OSX
	PG ?=
	INSTALL ?= brew install 
endif

INVE = ./inve
ARGS = $(filter-out $@, $(MAKECMDGOALS))
VER ?= 3.6
PYTHON = python$(VER)
PIP = pip$(VER)
MP ?= ./server/manage.py
ENV ?= dev
export DJANGO_SETTINGS_MODULE=settings.$(ENV)

run: .env
	$(INVE) $(MP) runserver 8000 --settings=settings.$(ENV)

mkenv:
	virtualenv .env --python=/usr/bin/$(PYTHON)

os-type:
	echo $(CCFLAGS)

help:
	less README.md

## usage make makemigration app=user
makemigration: .env
	$(INVE) $(MP) makemigrations ${app}

## usage make migrate app=user
migrate: .env
	$(INVE) $(MP) migrate ${app}

thumbnail:
	$(INVE) $(MP) makemigrations thumbnail

manage-create-user: .env
	$(INVE) $(MP) createsuperuser

manage-shell: .env
	$(INVE) $(MP) shell

make-static: .env
	$(INVE) $(MP) collectstatic

pip-freeze: .env
	$(INVE) pip freeze > requirements/pip_freeze.txt

del-pyc:
	find . -name "*.pyc" -exec rm -rf {} \;

## db
postgres-createuser:
	$(PG) createuser blog_user -P

postgres-dropuser:
	$(PG) dropuser blog_user

postgres-createdb:
	$(PG) createdb -O blog_user blog_db

postgres-dropdb:
	$(PG) dropdb blog_db

psql:
	psql -h localhost -U blog_user blog_db

psql-dropdb:
	psql -U postgres -c "drop database blog_db"

## project
setup-project:
	make postgres-createuser # blog_user/blog_passwd
	make postgres-createdb   # blog_db
	make migrate
	make makemigration app=core
	make makemigration app=post
	make makemigration app=user
	make makemigration app=multimedia
	make migrate
	make manage-create-user  # admin/qwerty12345
	$(INVE) $(MP) collectstatic
	make

reset-project:
	make postgres-dropdb
	make postgres-dropuser
	make setup-project

## python code utils
autoflake:
	autoflake --recursive --remove-all-unused-imports --remove-unused-variables server
autoflake-fix:
	autoflake --in-place --recursive --remove-all-unused-imports --remove-unused-variables server

autopep8:
	autopep8 --recursive --diff --aggressive --aggressive server
autopep8-fix:
	autopep8 --in-place --recursive --aggressive --aggressive server

pyflakes:
	python3 -m pyflakes server

yapf:
	yapf --diff --recursive server

## Front end tools ##
## https://thesocietea.org/2016/01/building-es6-javascript-for-the-browser-with-gulp-babel-and-more/

front-setup:
	$(INSTALL) node
	npm install gulp-cli -g
	npm install gulp -D
	npm install

front-install:
	npm install

front-watch:
	./node_modules/.bin/gulp

front-build:
	./node_modules/.bin/gulp build


## Base ##

.env: requirements.txt requirements/*.txt del-pyc
	test -d $@ || virtualenv -p $(PYTHON) --system-site-packages $@
	$(INVE) $(PIP) install -r requirements.txt
	@touch $@
