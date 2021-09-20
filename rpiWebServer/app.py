'''
	Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
from flask import Flask, render_template, request



app = Flask(__name__)




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 26

ledSts = 0


GPIO.setup(led, GPIO.OUT)   


GPIO.output(led, GPIO.LOW)

	
@app.route("/")
def index():
	
	ledSts = GPIO.input(led)
	templateData = {
              'title' : 'GPIO output Status!',
              'led'  : ledSts,
        }
	return render_template('index.html', **templateData)
	
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'led':
		actuator = led
   
	if action == "on":
		GPIO.output(actuator, GPIO.LOW)
	if action == "off":
		GPIO.output(actuator, GPIO.HIGH)
		     
	ledSts = GPIO.input(led)
   
	templateData = {
              'led'  : ledSts,
	}
	return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='ip', port=3000, debug=True)
