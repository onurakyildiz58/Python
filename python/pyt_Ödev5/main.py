
print("---------------problem 1---------------")
for i in ['a','b','c']:
    try:
        print(i*2)# "**" işlemi üs alma işlemidir print(i**2) hali hatalıydı çünkü string değişkenler sayısal işleme tabi tutulamaz
    except TypeError:
        print("TypeError hatası oluştu")
print()
print("---------------problem 2---------------")
x = 5
y = 1
try:
    z = x/y
except ZeroDivisionError:
    print("Sıfıra bölme hatası")#print fonksiyonun içi boştu bi değer çıkarmıyordu ama except bloğunun içine giriyordu hata almamak için y değişkeninin değerini değiştirdim
finally:
    print("Herşey tamam")
print()
print("---------------problem 3---------------")
def karebul():
    try:
        x=int(input("Tam sayı girin="))
        print(x, "sayısının karesi :",x**2)
        #while type(x) == int: while bloğu gereksiz olmuş zaten excep bloğu kontrol ediyor
        #    print(x ** 2)
        #    break
    except ValueError:
        print("Tam sayı girişi olmalı")
    else:
        print("her şey tamam")
karebul()
print()
print("---------------problem 4---------------")
try:
    f = open("C:/Users/onura/PycharmProjects/191307026_Onur_Akyıldız_Aktivite5/dosya.txt", "r")
    s = f.read()
    i = str(s.strip())# aktivite 4 te kullandığım txt dosyasını kullandım içeriği string olduğu için değer hatası aldım int değişkenini str ile değiştirdim
    print(type(i), i)
except FileNotFoundError:
    print("Dosya Bulunamadı")
except ValueError:
    print("Değer hatası")
except NameError:
    print("Satırdaki değişken bulunamadı")
except IndentationError:
    print("Yanlış girinti sözdizimi hatası")
print()
print("---------------problem 5---------------")

def sayıcarpımı(x,y):
    try:
        print(x*y)
    except :
        raise NameError('Sayılar int değil')
try:
    sayıcarpımı(2, 2.3)# str ile int herhangi bi sayısal işleme tabi tutulamaz
except NameError as msg:
    print(msg)
print()
print("---------------problem 6---------------")

def lowr(s):
    s.lower()
    return s[0].upper()+s[1:]
try:
    print(lowr('asdwqd'))
    assert lowr('asdwqd') == 'Asdwqd'
except AssertionError:
    print("Assertion hatası")
else:
    print("assertion hatası yok")
