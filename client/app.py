from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    response = requests.get('http://localhost:5000/')
    myjson = response.json()
    songs = myjson['songs']
    return render_template('index.html', songs=songs)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
