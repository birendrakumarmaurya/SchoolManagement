# routes/auth_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from config import get_db_connection

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def home():
    return render_template("login.html")

@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        session["username"] = user["username"]
        return redirect(url_for("auth.dashboard"))
    else:
        return "Invalid credentials"

@auth_bp.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("auth.home"))
    return f"Welcome {session['username']}!"
