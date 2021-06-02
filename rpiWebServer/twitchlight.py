'''
	Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import time


app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#define actuators GPIOs
ledRed = 26
#initialize GPIO status variables
ledRedSts = 0

# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)   

# turn leds OFF 
GPIO.output(ledRed, GPIO.LOW)

	
@app.route("/")
def index():
	# Read Sensors Status
	ledRedSts = GPIO.input(ledRed)
	templateData = {
              'title' : 'GPIO output Status!',
              'ledRed'  : ledRedSts,
        }
	return render_template('index.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'ledRed':
		actuator = ledRed
   
	if action == "on":
		GPIO.output(actuator, GPIO.LOW)

		time.sleep(5)
		GPIO.output(actuator, GPIO.HIGH)
		
	ledRedSts = GPIO.input(ledRed)
   
	templateData = {
              'ledRed'  : ledRedSts,
	}
	return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='192.168.0.31', port=3000, debug=True)
