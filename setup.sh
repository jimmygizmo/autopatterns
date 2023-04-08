#! /usr/bin/env bash


# Install the latest Python into your Pyenv: pyenv install 3.11.2
# This project is configured to use the virtual environment name of "ve.autopat"

# pyenv virtualenv 3.11.2 ve.autopat


pip install --upgrade pip
pip install --upgrade setuptools
pip install --upgrade wheel

pip install -r requirements.txt

