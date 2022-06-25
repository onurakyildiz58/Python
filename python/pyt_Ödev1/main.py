#onur akyıldız 191307026
import math
kosul = 0

while True:
    sart = int(input("bi değer giriniz : "))
    if sart <= kosul:
        break
    if sart > kosul:
       for a in range(0, 11):
           for b in range(10, 0, -1):
               for m in range(0,sart):
                   if abs(a - b) % sart == m:
                       if m == sart-1:
                           print("kalan sınıfı ", m, " = ", end="")
                           print("(", a, ",", b, ")")
