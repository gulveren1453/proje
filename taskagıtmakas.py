import random


def bsyr_secimi_uret():
    n=random.randint(1, 3)
    if n==1:
        return "tas"
    elif n==2:
        return "makas"
    else:
        return "kagit"
skor_kullanici=0
skor_bilgisayar=0 

while True:
    kullanici_secimi=input("tas? kagıt? makas?")
    bilgisayar_secimi=bsyr_secimi_uret()

    print("bilgisayar:",bilgisayar_secimi)

    if bilgisayar_secimi==kullanici_secimi:
        print("berabere")
    elif bilgisayar_secimi =="tas" and  kullanici_secimi=="makas":
        skor_bilgisayar+=1
    elif bilgisayar_secimi =="tas" and  kullanici_secimi=="kagit":
        skor_kullanici+=1
    elif bilgisayar_secimi =="makas" and  kullanici_secimi=="tas":
          skor_kullanici+=1
    elif bilgisayar_secimi =="makas" and  kullanici_secimi=="kagit":
       skor_bilgisayar+=1  
    elif bilgisayar_secimi =="kagit" and  kullanici_secimi=="tas":
       skor_bilgisayar+=1   
    elif bilgisayar_secimi =="kagit" and  kullanici_secimi=="makas":
        skor_kullanici+=1     


    print("Siz:",skor_kullanici,"VS bsyr:",skor_bilgisayar)

    if skor_kullanici==3 or skor_bilgisayar==3:
        break
if skor_bilgisayar>skor_kullanici:
    print("Kayebettiniz")
else:
    print("Kazandınız")     
    
