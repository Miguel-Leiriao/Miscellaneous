import time
import RPi.GPIO as GPIO
import serial

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

while True:
    print "Atempting Detection..."

    intruder=GPIO.input(11)
    print "intruder", intruder
    if intruder == 0:
        print "No intruders", intruder
        time.sleep(1)

    elif intruder == 1:
        print "intruder detected", intruder
        deviceID  = "0001"
        message = "IntruderDetected"
	time.sleep(1)

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
	data = ser.read(10)
	time.sleep(1)


	ser.write("AT\r\n")
	data = ser.read(10)
	print "AT: ", data

	if "OK" in data:

		ser.write("AT+NBAND=20"+"\r\n")
		data1 = ser.read(10)
		print "Adjust band: ", data1

		ser.write("AT+COPS=1,2,\"*****\""+"\r\n")
		data2 = ser.read(10)
		print "Select Network: ", data2

	else:
		print "Cant read AT command"


	if "OK" in data1 and "OK" in data2:

		ser.write("AT+NUESTATS"+"\r\n")
        	data4 = ser.read(150)
		print "STATUS: ", data4

		ser.write("\r\nAT+CGATT?"+"\r\n")
        	data5 = ser.read(30)
		print "CGATT: ", data5

		ser.write("\r\nAT+CSQ"+"\r\n")
        	data6 = ser.read(10)
		print "CSQ: ", data6

		ser.write("\r\nAT+CGPADDR"+"\r\n")
        	data7 = ser.read(40)
		print "Address: ", data7

		print "Creating Socket..."
		ser.write("AT+NSOCR=DGRAM,17,2020"+"\r\n")
        	data8 = ser.read(20)
		print "Socket created", data8

		print "Writing..."
		ser.write("AT+NSOST=0,URL,2020,1,81"+"\r\n")
        	data9 = ser.read(20)

		if "OK" in data9:
			print "Done Writing message", data9
		else:
			print "ERROR in sending message"

		print "Closing socket..."
		ser.write("AT+NSOCL=0"+"\r\n")
		data10 = ser.read(100)
		print "Closed", data10
		time.sleep(2)
