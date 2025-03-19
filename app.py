from flask import Flask, render_template

import json

app = Flask(__name__)
def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)

@app.route('/')
def home():
    shows = load_data()
    return render_template('index.html', shows=shows)

if __name__ == '__main__':
    app.run()