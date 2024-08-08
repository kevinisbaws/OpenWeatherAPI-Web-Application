from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

session = Session()

@app.route('/', methods = ['GET', 'POST'])
def index():
  if (request.method == "POST"):
    city = request.form.get("city")

    

