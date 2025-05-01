from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Привет из Flask, задеплоенного через Ansible!"
