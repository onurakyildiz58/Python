from functools import reduce

print("1-k. en küçük elemanı bulma")
print("2-En yakın çifti bulma")
print("3-Aynı isimli kisiye ait cocukları sırala")
print("4-Bir listedeki tekrar edenleri bulma")
print("5-Matris çarpımı")
print("6-Bir text içindeki kelimelerin frekansını bulma")
a = int(input("hangi işlemi istiyorsanız karşılığındaki numarayı giriniz : "))
print()

def durum(a):
    if a == 1:
        liste=[]
        length=int(input("liste kaç elemanlı istiyorsanız girin : "))
        for i in range(length):
            print(i + 1, ".sayı = ", end="")
            member = int(input())
            liste.append(member)
        print("kaçıncı küçük elemanı istiyorsunuz : ", end="")
        kucuk = int(input())
        print(kthkucuk(kucuk, liste))
    elif a == 2:
        liste = []
        length = int(input("liste kaç elemanlı istiyorsanız girin : "))
        for i in range(length):
            print(i + 1, ".sayı = ", end="")
            member = int(input())
            liste.append(member)
        print("en yakın sayı : ", end="")
        sayi = int(input())
        print(encift(liste, sayi, length))
    elif a == 3:
        kisiler_listesi = ["Fadime Ayse Mehmet", "Ali Nurhan Hasan", "Selim Betül Mehmet", "Ahmet Ayse Osman", "Onur Ebru Ferhat", "Berke Zeynep Emre", "Arda Nurhan Dursun"]
        cocuklar(kisiler_listesi)
    elif a == 4:
        liste = []
        length = int(input("liste kaç elemanlı istiyorsanız girin : "))
        for i in range(length):
            print(i + 1, ".sayı = ", end="")
            member = int(input())
            liste.append(member)
        tekrar(liste)
    elif a == 5:
        listesayi = []
        length = int(input("liste kaç elemanlı istiyorsanız girin : "))
        for i in range(length):
            print(i + 1, ".sayı = ", end="")
            member = int(input())
            listesayi.append(member)
        listeisim = []
        for i in range(length):
            print(i + 1, ".isim = ", end="")
            member = str(input())
            listeisim.append(member)
        matris(listeisim, listesayi)
    elif a == 6:
        try:
            dosya = open("C:/Users/onura/PycharmProjects/dosya.txt", "r")
            icerik = dosya.read()
            print(textfrekans(icerik))
            dosya.close()
        except FileNotFoundError:
            print("dosya bulunamadı")

def encift(liste, sayi, uzunluk):
    """
        listedeki hangi 2 sayını toplamı girilen sayıya daha yakındır

        :arg:
            liste (list): elemanları tek tek toplanacak liste
            sayi (int): kullanıcıdan alının sayı
        :return:
            ikili (list): listenin her hangi iki elemanı
    """
    listsorted=sorted(liste)
    farklist=[]
    uzun=uzunluk*(uzunluk - 1)
    for i in range(len(liste)):
        for j in range(len(liste)):
            if not i == j:
                for k in range(uzunluk):
                    a = listsorted[i]+listsorted[j]
                    fark = abs(sayi - a)
                    farklist.append(fark)

    print(farklist)
    print(list(set(farklist)))


def cocuklar(kisiler_listesi):
    cocuk = []
    for i  in kisiler_listesi:
        cocuk.append([isim_al(i), i])
    print("kişiler listesi : ", kisiler_listesi)
    print("çocuklar listesi : ", sorted(cocuk))
    for j in range(len(kisiler_listesi)):
        for k in range(len(kisiler_listesi)):
            if cocuk[j] == cocuk[k]:
                print(cocuk[k])
def isim_al(i):
    return i.split(" ")[1]
def tekrar(liste):
    """
        listedeki tekrarlanan sayıları bulma

        :arg:
        liste (list): tekrar edenleri bulacağımız liste

        :return:
        tekrareden (int): tekrar edenler
    """
    tekrarlar=[]
    listeyeni = sorted(liste)
    for i in range(len(liste)):
        for j in range(len(liste)):
            if not i == j:
                if listeyeni[i] == listeyeni[j]:
                    tekrarlar.append(listeyeni[i])
    print(list(set(tekrarlar)))
def kthkucuk(kucuk, liste):
    """
        kaçıncı en küçük eleman bulma

        bir listede x. en küçük elam ne ise onu döner

        :arg:
            liste (list): sıralanacak liste
            kucuk (int): kaçıncı elemanı istiyorsak o

        :return:
            k. en küçük eleman
    """
    kucukhal = sorted(liste)
    return kucukhal[kucuk-1]
def matris(isim, sayi):
    """
        girilen iki listeyi zipleyip birleştiren fonksiyon
        :arg:
            isim (list): isimlerin olduğu liste
            sayi (list): sayiların olduğu liste
        :return:
            list(zip1) (list): birleştirilmiş liste
    """
    zip1 = zip(isim, sayi)
    print(list(zip1))
    """
        not: tam olarak bu kısımda ne yapıyor anlamadım 
        A = [[1, 2, 3], [4, 5, 6]]
        B = [[7, 8], [9, 10], [11, 12]] ise
        sonuc= [[58, 64], [139, 154]]
    """
def textfrekans(dosya):
    """
        textte şu kelimeden kaç tane var
        :arg:
            dosya (list): textten okuduğum verileri splip ile kelime kelime ayırıp listeye atadım
        :return:
            counter (dict): tekrar eden ve sayısını dictionary olarak döndürdüm
    """
    print("dosya içeriği : ", dosya)
    dosyalist = dosya.split()
    print("liste hali : ", dosyalist)
    dosyasıra = sorted(dosyalist)
    counter = {}
    for letter in dosyalist:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

durum(a)