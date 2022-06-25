#!/bin/bash

cd portfolio
git fetch
git reset origin/main --hard
python -m venv python3-virtualenv
source python-virtualenv/bin/activate
pip install -r requirements.txt
Restart myportfolio service
