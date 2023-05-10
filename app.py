from flask import Flask

app = Flask(__name__)

@app.route('/')
def halo():
    return "Satria Dhapa Hamdani"