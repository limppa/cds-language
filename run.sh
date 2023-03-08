#!usr/bin/env bash

# create virtual environment
python3 -m venv spacy_env

# activate virtual environment
source ./spacy_env/bin/activate
# then install requirements
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m spacy download en_core_web_md

# run the code
python3 src/script.python3

# deactivate the venv
deactivate