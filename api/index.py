from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query_metabolite', methods = ['POST'])
def query_metabolite():
    query = request.form['query_metabolite']
    return render_template('query_result.html', metabolite=query_metabolite)


if __name__ == "__main__":
    app.run(debug = True)