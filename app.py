# Login Authentication System using Flask
# Full authentication code will be added here soon.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Login Authentication System - Coming Soon!"

if __name__ == "__main__":
    app.run(debug=True)
