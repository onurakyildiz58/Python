#191307026 onur akyıldız

import math
import colorama
from colorama import Fore, Style
colorama.init()

print("1-Gireceğiniz sayılardan en küçük değeri bulma")
print("2-Fibonacci sayı dizisi")
print("3-Satrançta atın gidebileceği kareler")
print("4-Machin formülü ile pi'yi bulma")
print("5-ikinci dereceden kökleri bulmak")
print("6-Mükemmel sayılar")
a=int(input("hangi işlemi istiyorsanız karşılığındaki numarayı giriniz = "))
print()


def durum(a):
    if a == 1:
        print("girilen sayılardan en küçüğü hangisi")
        list = []
        tane = int(input("listeye kaç tane sayı gireceksiniz yazınız = "))
        for min in range(tane):
            sayilar = int(input("sayı giriniz = "))
            list.append(sayilar)
        enkucuksayi(list)
        print()
    elif a == 2:
        print("fibonacci sayı dizisi")
        fib()
        print()
    elif a == 3:
        print("at hangi karelere gidebilir")
        satir = int(input("atın bulunduğu konumdaki satır bilgisini giriniz \"1-2-3-4-5-6-7-8\" = "))
        sutun = int(input("atın bulunduğu konumdaki sütun bilgisini giriniz \"1-2-3-4-5-6-7-8\" = "))
        satranc_at(satir, sutun)
        print()
    elif a == 4:
        print("pi'yi bulalım")
        bulPi()
        print()
    elif a == 5:
        print("ikinci dereceden denklemkerin kökleri")
        print("denkleminizdeki kat sayıları yazınız")
        a = int(input("x**2 li ifadenin kat sayısı = "))
        b = int(input("x li ifadenin kat sayısı = "))
        c = int(input("sabit terimin kat sayısı = "))
        kökbul(a,b,c)
        print()
    elif a == 6:
        print("mükemmel sayılar") #(2**(p-1) * (2**p - 1))
        mükemmel()
        print()


def enkucuksayi(sayi):
        enkucuk = sayi[0]
        enbuyuk = sayi[0]
        for n in sayi:
            if enkucuk > n:
                enkucuk = n
            if enbuyuk < n:
                enbuyuk = n
        print("en küçük sayı ",enkucuk , "\nen büyük sayı ",enbuyuk)

def fib():
    sınır = int(input("kaç elemanlı bi fibonacci dizisi istersiniz = "))
    a = 0
    b = 1
    print(a, b, end=" ")
    for f in range(2, sınır):
        toplam = a + b
        print(toplam, end=" ")
        a = b
        b = toplam

def bulPi():
    pi = 4*(4*(math.atan(1/5)) - (math.atan(1/239)))
    print(pi)

def kökbul(a,b,c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        x1 = (- b - delta ** 0.5) / (2 * a)
        x2 = (- b + delta ** 0.5) / (2 * a)
        print("denklemin reel kökü yoktur bunlar ", x1, x2, " dir")
    elif delta > 0:
        x1 = (- b - delta ** 0.5) / (2 * a)
        x2 = (- b + delta ** 0.5) / (2 * a)
        print("denklemin 2 farklı reel kökü vardır bunlar ", x1, x2, " dir")
    else:
        x4 = (- b + delta ** 0.5) / (2 * a)
        x1 = (- b - delta ** 0.5) / (2 * a)
        if x4 == x1:
            print("denklemin çakışık (aynı) 2 kökü vardır bunlar ", x4, " dir")

def mükemmel():
    for f in range(2,20):
        t = 0
        for i in range(2,f):
            if f % i == 0:
                t = t+1
        if t == 0:
            formül = (2 ** (f - 1) * (2 ** f - 1))
            if formül < 10000:
                print(formül)

def satranc_at(satır, sutun):
    satırtemp1 = satır
    sutuntemp1 = sutun
    satırtemp2 = satır
    sutuntemp2 = sutun
    # at L şeklinde 3 ileri 2 sağa ya da sola 3 geri sağa ya da sola gider
    temp = ["A", "B", "C", "D", "E", "F", "G", "H"]
    print("satranç tahatası şu sekildedir at + ile gördüğünüz konumdadır")
    tahta = [['*', '*', '*', '*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*', '*', '*', '*']]
    #for a in range(len(tahta)):
        #for b in range(len(tahta[a])):
            #print(tahta[a][b], end='  ')
        #print()
    print("    1    2    3    4    5    6    7    8")
    for a in range(len(tahta)):
        print(temp[a], end=' ')
        for b in range(len(tahta[a])):
            if a == satır-1 and b == sutun-1:
                print(end="  ")
                print(Fore.RED, end='')
                print("+", end='  ')
                print(Style.RESET_ALL, end='')
                continue
            print(end="  ")
            print("*", end='  ')
        print()
    # 3 ileri 1 sağ
    # 3 ileri 1 sol
    # 3 geri 1 sağ
    # 3 geri 1 sol
    # 3 sağa 1 ileri
    # 3 sağa 1 geri
    # 3 sola 1 ileri
    # 3 sola 1 geri

    # 1 ileri 3 sağ
    # 1 ileri 3 sol
    # 1 geri 3 sağ
    # 1 geri 3 sol
    # 1 sağa 3 ileri
    # 1 sağa 3 geri
    # 1 sola 3 ileri
    # 1 sola 3 geri

    print("hangi yöne gitmek istediğinizi yazınız")
    print("1- ileri sağ")
    print("2- ileri sol")
    print("3- geri sağ")
    print("4- geri sol")
    print("5- sağ ileri")
    print("6- sağ geri")
    print("7- sol ileri")
    print("8- sol geri")
    at = int(input("gitmek istediğiniz yönün karşılığını yazınız = "))

    if at == 1:
        print()
        if satır - 2 >= 1 and sutun + 1 <= 8:#ileri sağ
            satırtemp1 = satırtemp1 - 2
            sutuntemp1 = sutuntemp1 + 1
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp1 - 1 and y == sutuntemp1 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        if satır - 1 >= 1 and sutun + 2 <= 8:#ileri sağ
            satırtemp2 = satırtemp2 - 1
            sutuntemp2 = sutuntemp2 + 2
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp2 - 1 and y == sutuntemp2 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        else:
            print("başarısız")

    elif at == 2:
        print()
        if satır - 2 >= 1 and sutun - 1 >= 1:#ileri sol
            satırtemp1 = satırtemp1 - 2
            sutuntemp1 = sutuntemp1 - 1
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp1 - 1 and y == sutuntemp1 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        if satır - 1 >= 1 and sutun - 2 >= 1:#ileri sol
            satırtemp2 = satırtemp2 - 1
            sutuntemp2 = sutuntemp2 - 2
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp2 - 1 and y == sutuntemp2 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        else:
            print("başarısız")

    elif at == 3:
        print()
        if satır + 2 <= 8 and sutun + 1 <= 8:#geri sağ
            satırtemp1 = satırtemp1 + 2
            sutuntemp1 = sutuntemp1 + 1
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp1 - 1 and y == sutuntemp1 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        if satır + 1 <= 8 and sutun + 2 <= 8:#geri sağ
            satırtemp2 = satırtemp2 + 1
            sutuntemp2 = sutuntemp2 + 2
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp2 - 1 and y == sutuntemp2 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        else:
            print("başarısız")

    elif at == 4:
        print()
        if satır + 2 <= 8 and sutun - 1 >= 1:#geri sol
            satırtemp1 = satırtemp1 + 2
            sutuntemp1 = sutuntemp1 - 1
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp1 - 1 and y == sutuntemp1 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        if satır + 1 <= 8 and sutun - 2 >= 1:#geri sol
            satırtemp2 = satırtemp2 + 1
            sutuntemp2 = sutuntemp2 - 2
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp2 - 1 and y == sutuntemp2 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        else:
            print("başarısız")

    elif at == 5:
        print()
        if satır + 2 <= 8 and sutun - 1 >= 1:#sağ ileri
            satırtemp1 = satırtemp1 + 2
            sutuntemp1 = sutuntemp1 - 1
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp1 - 1 and y == sutuntemp1 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        if satır + 1 <= 8 and sutun - 2 >= 1:#sağ ileri
            satırtemp2 = satırtemp2 + 1
            sutuntemp2 = sutuntemp2 - 2
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp2 - 1 and y == sutuntemp2 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        else:
            print("başarısız")

    elif at == 6:
        print()
        if satır + 2 <= 8 and sutun + 1 <= 8:#sağ geri
            satırtemp1 = satırtemp1 + 2
            sutuntemp1 = sutuntemp1 + 1
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp1 - 1 and y == sutuntemp1 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        if satır + 1 <= 8 and sutun + 2 <= 8:#sağ geri
            satırtemp2 = satırtemp2 + 1
            sutuntemp2 = sutuntemp2 + 2
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp2 - 1 and y == sutuntemp2 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        else:
            print("başarısız")

    elif at == 7:
        print()
        if satır-2 >= 1 and sutun-1 >= 1:#sol ileri
            satırtemp1 = satırtemp1 - 2
            sutuntemp1 = sutuntemp1 - 1
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp1 - 1 and y == sutuntemp1 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        if satır-1 >= 1 and sutun-2 >= 1:#sol ileri
            satırtemp2 = satırtemp2 - 1
            sutuntemp2 = sutuntemp2 - 2
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp2 - 1 and y == sutuntemp2 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        else:
            print("başarısız")

    elif at == 8:
        print()
        if satır-2 >= 1 and sutun+1 <= 8:#sol geri
            satırtemp1 = satırtemp1 - 2
            sutuntemp1 = sutuntemp1 + 1
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp1 - 1 and y == sutuntemp1 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        if satır-1 >= 1 and sutun+2 <= 8:#sol geri
            satırtemp2 = satırtemp2 - 1
            sutuntemp2 = sutuntemp2 + 2
            print("atın yeni konumu")
            print("    1    2    3    4    5    6    7    8")
            for x in range(len(tahta)):
                print(temp[x], end=' ')
                for y in range(len(tahta[a])):
                    if x == satırtemp2 - 1 and y == sutuntemp2 - 1:
                        print(end="  ")
                        print(Fore.RED, end='')
                        print("+", end='  ')
                        print(Style.RESET_ALL, end='')
                        continue
                    print(end="  ")
                    print("*", end='  ')
                print()
        else:
            print("başarısız")

durum(a);