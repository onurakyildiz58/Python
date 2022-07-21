import colorama
from colorama import Fore, Style
colorama.init()
try:
    from sympy.mpmath import mp
except ImportError:
    from mpmath import mp

def bol(str):
    liste = []
    liste[:0] = str
    return liste

def birlestir(s):
    STR = ""
    for ele in s:
        STR += ele
    return STR


mp.dps = 10000 # pi'nin uzunluğu
print(mp.pi)
# rivayete göre pi sayısı o kadar sayı kümesi barındırırki içinde banka şifreniz bile olabilir
# bölme işlemi sonucu olduğu için içinde 0 olması imkansızdır aksi halde pi sayısı sonlu olacaktır çünkü tam bölünür
# buldurmak istediğiniz sayının içinde 0 olmasın

x = str(input("bulunacak ifadeyi giriniz : "))
uzunluk = len(x)

if x in str(mp.pi):
    index = str(mp.pi).find(x)
    print("şu indexte bulundu ", index)
    listee = bol(str(mp.pi))
    once = birlestir(listee[0:index])
    orta = birlestir(listee[index:uzunluk+index])
    son = birlestir(listee[uzunluk+index+1:mp.dps])
    print(Fore.RESET + once + Fore.RED + orta + Fore.RESET + son)



else:
    print("sayı yoktur")