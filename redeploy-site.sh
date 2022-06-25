#!/bin/bash
cd portfolio
git fetch
git reset origin/main --hard
python -m venv python-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
systemctl daemon-reload
systemctl restart myportfolio
systemctl status myportfolio
