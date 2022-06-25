
# ders bir
print()
print("*"*20)
sayi = 5
sayi1 = 10
toplam = sayi1+sayi
print(sayi1, sayi, sep="+", end="=")
print(toplam)
print('''çok
satırlı açıklama 
 
satırı''')

# ders iki
print()
print("*"*20)
print(5+7)
print(7-5)
print(5-7)
print(5*7)
print(22/7)#küsüratlı böler
print(7//5)#tam böler
print(2**10)#üs alır
print(9 % 5)# mod

#ders üç
print()
print("*"*20)
# << sola bir bit kaydırma
# >> sağa bir bit kaydırma
# & ve anlamına gelir (and)
# | veya anlamına gelir (or)
# ~ bitwise değil anlamına gelir
a = 10 #10 decimal saysısı 1010 binary sayısına eşittir
b = 4 #4 decimal sayısı 0100 binary sayısına eşittir
print(a & b) # yapmış olduğu işlem 10 ve 4 decimal sayısına ait her bir biti kendi arasında (and) ve operatörü ile karşılaştırması
# 1010 & 0100 = ?
# ve komutunda:
# 1 ve 1 = 1
# 1 ve 0 = 0
# 0 ve 1 = 0
# 0 ve 0 = 0 yani mutlaka şartlardan ikiside doğru olmalı
# sonuç: (0000)2 = (0)10
print(a | b) # yapmış olduğu işlem 10 ve 4 decimal sayısına ait her bir biti kendi arasında (or) veya operatörü ile karşılaştırması
# 1010 & 0100 = ?
# veya komutunda:
# 1 ve 1 = 1
# 1 ve 0 = 1
# 0 ve 1 = 1
# 0 ve 0 = 0 yani şartlardan biri doğru olsa yeter
# sonuç: (1110)2 = (14)10
print("10 sayısının bit düzeyinde değili : ", ~a)
print("4 sayısının bit düzeyinde değili : ", ~b)
#çalışma mantığı
#10 = 1010
#~10 = ~1010
#    = -(1010 + 1)
#    = -(1011)
#    = -11
print("10 sayısının bir bit sağa kaymış hali : ", a >> 1)#0000 1010 -> 0000 0101 = 5
print("4  sayısının 2 bit sola kaymış hali : ", b << 2)#0000 0100 -> 0001 0000 = 16

#ders dört
print()
print("*" * 20)
str = "first step for learning python."
str2 = 'Ok its not firts but im gonna learn thoroughly.'
print(str, str2)
print(str[3])
print(str[6:10])#arasındaki indisleri basar
print(str[:15])#baştan istenilene kadar yazar
print(str[::-1])#tersten yazar