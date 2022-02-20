#!/bin/bash

set -e

# TODO: check that python3 exists
# TODO: check that virtualenv exists

if [ ! -d env ]; then
  echo "env directory not found. Creating it..."
  python3 -m virtualenv env
  ./env/bin/pip3 install -r requirements.txt
  ./env/bin/python3 manage.py migrate
fi

./env/bin/python3 manage.py runserver
