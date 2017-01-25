import os
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_env():
    return json.dumps({k: v for k, v in os.environ.items()}, indent=2)
