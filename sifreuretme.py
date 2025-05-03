import random
import string#tek tek yazmam yerine hepsini içeren kütühane 


rakamlar=string.digits
semboller=string.punctuation
kucuk_harfler=string.ascii_lowercase
buyuk_harfler=string.ascii_uppercase

tum_karakterler=[rakamlar,semboller,kucuk_harfler,buyuk_harfler]

    
    
for j in range(2):
    for i in range(1):
        sifre+=tum_karakterler[j][random.randint(0, len(tum_karakterler[i])-1))]
    
    
sifre=list(sifre)
random.shuffle(sifre)
print(sifre)
yeni_sifre=""
for i in sifre:
    yeni_sifre+=i
print(yeni_sifre)    
