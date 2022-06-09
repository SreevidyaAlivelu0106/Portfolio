import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('workex_ed_sree.html', title="Sree Info", url=os.getenv("URL"))



@app.route('/sree_hobbies')
def sree_hobbies():
    return render_template('hobbies_template_sree.html', title="sree's Hobbies", url=os.getenv("URL"))
