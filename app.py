# Imports.
from flask import Flask, render_template, request, jsonify
from db import Database

# Initialization.
app = Flask(__name__)
db = Database()


# Route - Landing Page
@app.route("/")
def landing_page():
    return render_template("index.html")


# Route - Leaderboard Page
@app.route("/leaderboard")
def leaderboard_page():
    records = db.get_top_scores()
    return render_template("leaderboard.html", players=records)


# Endpoint - User score update
@app.route("/api/add-score", methods=["POST"])
def update_score():
    data = request.json
    username = data.get("username")
    score = data.get("score")

    if not username or not score:
        return jsonify({"error": "Username and Score required"}), 400

    db.update_score(username, score)

    return jsonify({"message": "Score Updated"}), 201
