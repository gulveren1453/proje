#♦fonksiyonlara gırıs ve fonksiyon okuryazarlığı 

def kare_al(x):
    print(x**2)

kare_al(5)    

def kare_al(x):
    print("girilen sayi :" +str(x) +" karesi:" + str(x**2))
  
kare_al(5)

#iki argümalı fonksiyon tanımlamak

def carpma_yap(x,y):
    print("sonuc: "+str(x*y))

carpma_yap(4, 5)    
#♦ön tanimli argumanlar 
def carpma_yap(x,y=5):
    print("sonuc: "+str(x*y))  

carpma_yap(4)

#argumanların siralamasi

carpma_yap(y=2,x=9)

def direk_hesap(isi,nem,sarj):
   return ((isi+nem)/sarj)

sonuc=direk_hesap(25, 50, 80)*5
print(sonuc)    

#◘local ve global değişkenler 
x=10
z=20
def carpma(x,z):
    return x*z
carpma(2,3)

#▼local etki alanından global etki alanini degistirmek
x=[]
def eleman_ekle(y):
    x.append(y)
    print(str(y)+" ifadesi eklendi")

eleman_ekle(2)
x
#karar&kontrol yapıları

#if
sinir=50000
gelir1=60000
gelir2=50000
gelir3=35000

if gelir2>sinir:
    print("tebriklerrr")
elif gelir2<sinir:
    print("uyarı!")
else:
    print("takibe devam")
    
#mini uygulama 
magaza_adi=input("mağaza adı nedir?")
gelir=int(input("gelirinizi giriniz:"))
sinir=50000
if gelir>sinir:
    print("tebriklerrrrr: "+magaza_adi)
elif gelir<sinir:
    print("uyarıııı!cok düsük gelir :"+str(gelir))
else:
    print("takibe devam")
    
#DONGULER -for

ogrenci=["ali","veli","isik","berk"]

for i in ogrenci:
    print(i)
    
#dongü ve fonksiyonları birlikte kullanmak
maaslar=[1000,2000,3000,4000,5000]
#maaslara yüzde 20 zam yapılacak kodları yaz

def zam():
    for j in maaslar:
        print(((j*20)/100)+j)

zam()        

#mini uygulama
#3000 tl den büyük yüzde 10 az sa yüzde 20
def yüzde_20(x):
    print((x*20/100)+x)

def yüzde_10(z):
    print((z*10/100)+z)
    
for i in maaslar:
    if i<3000:
       yüzde_20(i)
    elif i>3000:
        yüzde_10(i)
    else:
        print("zam yok.")

#break-contiune

maaslar=[8000,5000,2000,1000,3000,7000,1000]
maaslar.sort()
maaslar

for i in maaslar:
    if i==3000:
        print("kesildi")
        break
    print(i)

for i in maaslar:
      if i==3000:
          continue
      print(i)
#While
sayi=1
while sayi<10:
    sayi+=1
    print(sayi)



          
     
     





























    
    