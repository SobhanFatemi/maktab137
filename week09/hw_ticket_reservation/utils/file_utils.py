<<<<<<< HEAD
import json
import os

def ensure_file(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f)

def load_json(path):
    ensure_file(path, [])
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
=======
import json
import os

def ensure_file(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f)

def load_json(path):
    ensure_file(path, [])
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
        json.dump(data, f, indent=4)