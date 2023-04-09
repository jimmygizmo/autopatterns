#! /usr/bin/env bash


# Install the latest Python into your Pyenv: pyenv install 3.11.2
# This project is configured to use the virtual environment name of "ve.autopat"

# pyenv virtualenv 3.11.2 ve.autopat

# Pip and Setuptools both come along with a fresh virtual environment and they ALWAYS need immediate upgrading.
pip install --upgrade pip
pip install --upgrade setuptools

# Wheel enables installation of Python modules using native-compiled components, and more.
pip install wheel

# Pip-tools simplifies the management of version-pinned Python requirements.
pip install pip-tools

pip install -r requirements.txt

