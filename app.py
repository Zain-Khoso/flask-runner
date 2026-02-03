# Imports.
from flask import Flask, render_template

# Initialization.
app = Flask(__name__)


# Route - Landing Page
@app.route("/")
def landing_page():
    return render_template("index.html")
