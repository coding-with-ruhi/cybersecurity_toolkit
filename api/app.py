from flask import Flask, render_template, request
from modules.password_checker import check_password_strength
from modules.cipher import encrypt, decrypt

app = Flask(__name__)

# Home
@app.route("/")
def home():
    return render_template("index.html")


# Password Checker
@app.route("/password", methods=["GET", "POST"])
def password():
    result = None
    feedback = []
    crack_time = None

    if request.method == "POST":
        user_password = request.form["password"]
        result, feedback, crack_time = check_password_strength(user_password)

    return render_template("password.html", result=result, feedback=feedback, crack_time=crack_time)


# Caesar Cipher
@app.route("/cipher", methods=["GET", "POST"])
def cipher():
    result = ""

    if request.method == "POST":
        text = request.form["text"]
        shift = int(request.form["shift"])
        action = request.form["action"]

        if action == "encrypt":
            result = encrypt(text, shift)
        else:
            result = decrypt(text, shift)

    return render_template("cipher.html", result=result)


# Image Tool
@app.route("/image")
def image():
    return render_template("image.html")


# Keylogger Demo
@app.route("/keylogger")
def keylogger():
    return render_template("keylogger.html")


# ALWAYS KEEP THIS AT THE END
if __name__ == "__main__":
    app.run(debug=True)