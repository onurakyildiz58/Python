import qrcode

code = qrcode.make('https://github.com/onurakyildiz58/Arduino-IoT-/tree/main/Proje%20B')

code.save('qrcode.png')