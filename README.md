docker exec template virtualenv /tmp/venv
docker exec template /tmp/venv/bin/pip install -r /tmp/requirements/requirements.dev.txt

