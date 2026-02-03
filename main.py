# Imports.
from flask import Flask

# Initialization.
app = Flask(__name__)


# Route - Landing Page
@app.route("/")
def landing_page():
    return '<h1 align="center">Flask - Runner</h1>'
