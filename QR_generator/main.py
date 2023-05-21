import qrcode

code = qrcode.make('https://www.youtube.com/shorts/0PgEIhXDMqY')

code.save('qrcode.png')