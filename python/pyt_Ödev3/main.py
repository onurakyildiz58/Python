#onur akyıldız 191307026

print("1-Gireceğiniz sayılardan en küçük değeri bulma")
print("2-Karekök bulma")
print("3-En büyük ortak böleni bulma")
print("4-Asallık testi")
print("5-Tuple üzerinde rekürsif uygulama")
a = int(input("hangi işlemi istiyorsanız karşılığındaki numarayı giriniz = "))
print()

def durum(a):
    if a == 1:
        liste=[]
        uzunluk = int(input("listenin uzunluğunu giriniz = "))
        print("istediğiniz sayıları tek tek listeye giriniz = ")
        for i in range(uzunluk):
            print(i + 1, ".sayı = ", end="")
            b = int(input())
            liste.append(b)
        print(enkucuk(liste))
    elif a == 2:
        kok = int(input("karekökü alınacak sayıyı giriniz = "))
        print(karekok(kok))
    elif a == 3:
        sayi1 = int(input("ilk sayıyı giriniz = "))
        sayi2 = int(input("ikinci sayıyı giriniz = "))
        print("girilen sayıların en büyük ortak böleni = ",ortakbolen(sayi1, sayi2))
    elif a == 4:
        prime = int(input("değer giriniz = "))
        print(asal(prime))
    elif a == 5:
        listetup1 = []
        print("4 elemanlı alt set değerlerini giriniz")
        for i in range(4):
            print(i + 1, ".sayı = ", end="")
            b = int(input())
            listetup1.append(b)
        listetup2 = []
        üsttset = int(input("üst set değerini giriniz = "))
        listetup2.append(üsttset)
        print(listetup1)
        print(listetup2)
        print(tupleislem(listetup1, listetup2))

def tupleislem(l1, l2):
    # recursive olarak yapamadım elimden bu geldi
    t1 = tuple(l1)
    t2 = tuple(l2)
    t3 = t1 + t2
    print(t3)
    print(type(t1), type(t2))
    for i in range(4):
        for j in range(4):
            if i == j:
                break
            elif t1[i] + t1[j] == t2[0]:
                return print(t1[i], "+", t1[j], "=", t2[0])
def enkucuk(listee):
    if len(listee) == 1:
        return listee[0]
    else:
        return min(listee[0], enkucuk(listee[1:]))
def asal(isPrime, i = 2):
    if (isPrime <= 2):
        return True if (isPrime == 2) else False
    if (isPrime % i == 0):
        return False
    if (i * i > isPrime):
        return True
    return asal(isPrime, i + 1)
def karekok(num):
    numf = float(num)
    maxiter = int(input("maxiter değerini giriniz = "))
    for i in range(maxiter):
        num = 0.5 * (num + numf / num)
    return num
def ortakbolen(first, second):
    if first < second:
        kucuk = first
    else:
        kucuk = second
    i = kucuk

    while i > 0:
        if first % i == 0 and second % i == 0:
            return i
        i = i - 1
    return 1
durum(a)