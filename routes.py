from flask import jsonify
import RPi.GPIO as GPIO
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 2

def index():
    return jsonify({'temperature': '/temperature', 'humidity': '/humidity'})

def temperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return jsonify({'temperature': temperature, 'units': 'celsius'})

def humidity():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return jsonify({'humidity': temperature, 'units': 'percent'})

def register(app):
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/temperature', 'temperature', temperature)
    app.add_url_rule('/humidity', 'humidity', humidity)
