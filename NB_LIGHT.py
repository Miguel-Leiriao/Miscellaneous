import time
import RPi.GPIO as GPIO
import os
#import threading


class DOOM():
	def setup():
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.setup(??, GPIO.OUT)
		GPIO.output(??, False)
	def button_callback(channel):
		print "HUURAY!!!"
		os.system("echo gpio | sudo tee /sys/class/leds/led1/trigger")
		UDP_comms()
		if "ORDER ON" in READING:
			GPIO.output(??, HIGH)
		if "ORDER OFF" in READING:
			GPIO.output(??, LOW)
		os.system("echo 0 | sudo tee /sys/class/leds/led1/brightness")
		time.sleep(1)
		os.system("echo 1 | sudo tee /sys/class/leds/led1/brightness")
	def conf():
		ser = serial.Serial(
		port='/dev/ttyUSB0',
		baudrate = 9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=3
		)
		ser.close()
		ser.open()
		print "port is open"

		ser.write("AT+CFUN=1\r\n")
		reboot = ser.read(10)
		time.sleep(1)

		ser.write("AT\r\n")
		AT = ser.read(10)
		print "AT: ", AT

		if "OK" in data:

			ser.write("AT+NBAND=20"+"\r\n")
			NBAND = ser.read(10)
			print "Adjust band: ", NBAND

			ser.write("AT+COPS=1,2,\"26806\""+"\r\n")
			NETWORK = ser.read(10)
			print "Select Network: ", NETWORK

		else:
			print "Cant read AT command"


		if "OK" in data1 and "OK" in data2:

			ser.write("AT+NUESTATS"+"\r\n")
        		NUESTATS = ser.read(150)
			print "STATUS: ", NUESTATS

			ser.write("\r\nAT+CGATT?"+"\r\n")
        		CGATT = ser.read(30)
			print "CGATT: ", CGATT

			ser.write("\r\nAT+CSQ"+"\r\n")
        		CSQ = ser.read(10)
			print "CSQ: ", CSQ

			ser.write("\r\nAT+CGPADDR"+"\r\n")
        		CGPADDR = ser.read(40)
			print "Address: ", CGPADDR
	def OpenGate():
		print "Creating Socket..."
		ser.write("AT+NSOCR=DGRAM,17,2020"+"\r\n")
        	Socket_created = ser.read(20)
		print "Socket created", Socket_created
	def CloseGate():
		print "Closing socket..."
		ser.write("AT+NSOCL=0"+"\r\n")
	def UDP_Comms():
		#print "Waiting for message"
		#ser.write("AT+NSOST=0,?????,2020,16,57616974696e6720666f722061757468"+"\r\n") 
		#data10 = ser.read(100)
		#print "message sent", data10
		#time.sleep(2)
		print "Reading message"
		ser.write("AT+NSORF=0,10"+"\r\n")
		READING = ser.read(100)
	setup()
	conf()
	OpenGate()
	print "wait for button press"
	GPIO.add_event_detect(40,GPIO.RISING,callback=button_callback)
while 1:
	DOOM()


