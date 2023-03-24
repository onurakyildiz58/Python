import serial

x = 0

#veriyi alma
uno = serial.Serial("com5", 9600)

while True:
    while uno.inWaiting() == 0:
        pass
    data = uno.readline()
    data = str(data, 'utf-8')
    print("gelen data : ", data)
