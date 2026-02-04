# Imports.
from flask import Flask, render_template, request, jsonify
from werkzeug.security import generate_password_hash
from db import Database

# Initialization.
app = Flask(__name__)
db = Database()


# Route - Landing Page
@app.route("/")
def landing_page():
    return render_template("index.html")


# Endpoint - User Sign Up
@app.route("/api/signup", methods=["POST"])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if db.get_user(username):
        return jsonify({"error": "User already exists"}), 409

    hashed_password = generate_password_hash(password)

    db.set_user(username, hashed_password)

    return jsonify({"message": "User created"}), 201
