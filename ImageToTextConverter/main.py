import pywhatkit as k
import flask


#art = ascii_magic.from_image_file('foxy.jpg')
#ascii_magic.to_terminal(art)


dosya = input(".jpg uzantılı dosya adını girin ")
k.image_to_ascii_art(dosya +'.jpg', dosya)
