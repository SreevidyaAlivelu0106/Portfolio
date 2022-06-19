#!/bin/bash
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
export FLASK_ENV=development
flask run --host=0.0.0.0
