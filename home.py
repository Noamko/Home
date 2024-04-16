import socket
import os
import sys

sys.path.append(f'{os.getcwd()}/ui')
from flask import Flask, render_template
app = Flask(__name__, template_folder='ui', static_folder='static')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dripitidrop")
def dripitidrop():
    return render_template("dripitidrop.html")
    
if __name__ == "__main__":
    app.run()