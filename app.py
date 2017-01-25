import os
import json
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def show_env():
    return json.dumps({k: v for k, v in os.environ.items()}, indent=2)


@app.route('/<path:path>')
def serve(path):
    return send_from_directory('.', path)
