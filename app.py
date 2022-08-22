import uuid

from flask import Flask
from flask import render_template, send_file, redirect

app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'success'


@app.route('/favicon.ico')
def favicon():
    return send_file('./favicon/favicon.ico', mimetype='image/png')


@app.route('/')
def home():
    return redirect("/uuid", code=302)


@app.route('/uuid')
def uuid_tool():
    return render_template('uuid.html',
        uuid_v1=str(uuid.uuid1()),
        uuid_v4=str(uuid.uuid4()))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
