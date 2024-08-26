from flask import Flask, request, render_template
import re
import random
import string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_password_strength", methods=["POST"])
def check_password_strength():
    password = request.form["password"]

    # Initialize strength score
    strength = 0

    # Check password length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters."

    # Check for digits
    if re.search(r"\d", password):
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for special characters
    if re.search(r"\W", password):
        strength += 1

    # Evaluate password strength
    if strength == 1:
        return "Password is weak. It should contain a mix of characters, numbers, and special characters."
    elif strength == 2:
        return "Password is medium. It should contain a mix of characters, numbers, and special characters."
    elif strength == 3:
        return "Password is strong. It contains a mix of characters, numbers, and special characters."
    elif strength == 4:
        return "Password is very strong. It contains a mix of characters, numbers, and special characters."

