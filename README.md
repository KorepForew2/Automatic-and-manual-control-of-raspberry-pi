To implement automatic and manual modes on Raspberry Pi for control based on process maps, you will need several components and approaches. Let's consider the main steps:

1. Hardware components
To implement a control system on Raspberry Pi, you may need the following devices:

Raspberry Pi
Sensors:
Soil moisture sensors
Temperature sensors
Light sensors
Water level sensors
Actuators:
Pumps for irrigation
Light bulbs
Fans for air circulation
Motors for controlling movement or plants
Relays for controlling pumps and lamps.
2. Installing and configuring Raspberry Pi
Install Raspberry Pi OS on the SD card and connect Raspberry Pi to the network.
Connect all sensors and actuators via GPIO ports. For this, you may need expansion boards or modules (e.g. I2C, SPI, or analog sensors).
3. Programming
You can use Python to develop the system, as it is well supported on Raspberry Pi and has many libraries for working with GPIO.

Example of the program structure:
The main logic will be divided into two modes:
Automatic mode, where the system will work according to the specified process maps.
Manual mode, where the user can manually enter parameters (e.g. watering, lighting, etc.).
Program plan:
3.1. Automatic mode
Process maps are sets of pre-set values ​​for each parameter (temperature, humidity, lighting, watering, etc.).
You must pre-set the acceptable ranges for each parameter.
In automatic mode, the system will check the current state using sensors and, if the values ​​are outside the acceptable ranges, it will take action (e.g. turn on pumps, turn on a fan, etc.).
python
import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)

# Example of control pins
pump_pin = 17
light_pin = 27

GPIO.setup(pump_pin, GPIO.OUT)
GPIO.setup(light_pin, GPIO.OUT)

# Control functions
def activate_pump():
GPIO.output(pump_pin, GPIO.HIGH) # Turn on the pump
print("Pump is on.")

def deactivate_pump():
GPIO.output(pump_pin, GPIO.LOW) # Turn off the pump
print("Pump is off.")

def activate_light():
GPIO.output(light_pin, GPIO.HIGH) # Turn on the light
print("Light is on.")

def deactivate_light():
GPIO.output(light_pin, GPIO.LOW) # Turn off the light
print("Lighting is off.")

# Example of a process chart (parameters can be specified in advance)
def automatic_mode(soil_moisture, temperature, light_level):
# Condition for automatic watering
if soil_moisture < 30:
activate_pump()
else:
deactivate_pump()

# Condition for lighting
if light_level < 50:
activate_light()
else:
deactivate_light()

# Condition for temperature control
if temperature > 30:
print("The temperature is high. Turning on the fan.")
elif temperature < 20:
print("The temperature is low. Need to heat it up.")

# Example sensors (you need to connect real sensors here)
soil_moisture = 25 # Example soil moisture value
temperature = 28 # Example temperature
light_level = 45 # Example light level

# Automatic mode
automatic_mode(soil_moisture, temperature, light_level)

# Finish working with GPIO
GPIO.cleanup()
3.2. Manual mode
In manual mode, the user can enter values ​​for all parameters and start processes manually via the interface or console.

python
def manual_mode():
print("Enabling manual mode:")
while True:
action = input("Enter the command (1 - turn on the pump, 2 - turn off the pump, 3 - turn on the light, 4 - turn off the light, q - exit): ")
if action == "1": 
activate_pump()
 elif action == "2":
 deactivate_pump()
 elif action == "3":
 activate_light()
 elif action == "4":
 deactivate_light()
 elif action == "q":
 break
 else:
 print("Invalid command. Try again.")

# Enabling manual mode
manual_mode()
4. Control via interface
For convenience, you can make an interface for control via a web interface using Flask or Django. In this interface, you can both change parameters and start/stop processes.

Example using Flask:
Install Flask:
bash
pip install flask
Simple web interface with control buttons:
python
from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

# Configuring GPIO
GPIO.setmode(GPIO.BCM)
pump_pin = 17
light_pin = 27
GPIO.setup(pump_pin, GPIO.OUT)
GPIO.setup(light_pin, GPIO.OUT)

@app.route('/')
def index():
return render_template('index.html')

@app.route('/turn_on_pump')
def turn_on_pump():
 GPIO.output(pump_pin, GPIO.HIGH)
 return 'Pump on!'

@app.route('/turn_off_pump')
def turn_off_pump():
GPIO.output(pump_pin, GPIO.LOW)
return 'Pump is off!'

@app.route('/turn_on_light')
def turn_on_light():
GPIO.output(light_pin, GPIO.HIGH)
return 'Light is on!'

@app.route('/turn_off_light')
def turn_off_light():
GPIO.output(light_pin, GPIO.LOW)
return 'Light is off!'

if __name__ == '__main__':
app.run(host='0.0.0.0', port=80)
index.html is a simple HTML file that will be used to display the interface.
5. Shutdown
It is important to always clean up GPIO resources after shutdown to avoid conflicts or hardware damage.

python
GPIO.cleanup()
6. Conclusions
You will need to create algorithms for automatic control using sensors and process charts, as well as implement a simple interface for manual control. All of these components can be combined into a single program on the Raspberry Pi to provide flexibility in control.
