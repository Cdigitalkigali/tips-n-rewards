# Third-party imports
from tempfile import mkdtemp
from flask import Flask, render_template
from cs50 import SQL
from flask_session import Session
# Local imports
from aux import *

# Configuration
db = SQL("sqlite:///main.db")
app = Flask(__name__)

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["PREFERRED_URL_SCHEME"] = 'https'
app.config["DEBUG"] = False
Session(app)

@app.route("/")
def index():
    return "Hello"
