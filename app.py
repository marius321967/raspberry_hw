from flask import Flask, jsonify

app = Flask('hello_world')

@app.route('/')
def index():
    return jsonify({"foo": "bar"}), 404

app.run()
