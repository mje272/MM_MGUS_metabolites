from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query_metabolite', methods = ['POST'])
def query_metabolite():
    metabolite = request.form['query_metabolite']
    ###### get this from dynamodb via lambda function
    mm_data = []
    mgus_data = []
    ######
    return render_template('query_result.html', metabolite=metabolite, mm_data=mm_data, mgus_data=mgus_data)


if __name__ == "__main__":
    app.run(debug = True)