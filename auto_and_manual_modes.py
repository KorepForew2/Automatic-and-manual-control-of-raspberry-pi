from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

# Настройка GPIO
GPIO.setmode(GPIO.BCM)
pump_pin = 17
light_pin = 27
GPIO.setup(pump_pin, GPIO.OUT)
GPIO.setup(light_pin, GPIO.OUT)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/turn_on_pump")
def turn_on_pump():
    GPIO.output(pump_pin, GPIO.HIGH)
    return "Насос включен!"


@app.route("/turn_off_pump")
def turn_off_pump():
    GPIO.output(pump_pin, GPIO.LOW)
    return "Насос выключен!"


@app.route("/turn_on_light")
def turn_on_light():
    GPIO.output(light_pin, GPIO.HIGH)
    return "Освещение включено!"


@app.route("/turn_off_light")
def turn_off_light():
    GPIO.output(light_pin, GPIO.LOW)
    return "Освещение выключено!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
