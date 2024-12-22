#!/bin/sh
# Start Xvfb in the background
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99
export PYTHONPATH=/app/
# Sleep pour laisser Xvfb démarrer
sleep 2
exec python src/main.py --server.headless true
