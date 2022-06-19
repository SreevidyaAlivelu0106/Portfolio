#!/bin/bash
pkill -f tmux
cd portfolio
git fetch
git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

dnf install tmux
tmux new -s "remote" -d
tmux send-keys -t "remote" "./ss.sh" C-m
tmux attach -t "remote" -d
