sayi1=int(input("bir sayi giriniz: "))
sayi2=int(input("bir sayi giriniz: "))
sayi3=int(input("bir sayi giriniz: "))

min=sayi1

if sayi2<min:
    min=sayi2
if sayi3<min:
    min=sayi3

print("minimum number is : " + str(min))    

sayi=int(input("uzun kenarı giriniz: "))
sayi4=int(input("kısa kenarı giriniz: "))
alan=sayi*sayi4
print("alan: "+ str(alan))


answ='y'
while answ=='y':
    sayi5=int(input("sayi giriniz: "))
    if(sayi5%2==0):
        print("this number is even.")
    
    if(sayi5%2!=0):
        print("this number is odd.")
    
    print("do you want another number(y/n)")
    answ=input("cevabını gir: ")
 
answ='y'
while answ=='y':
    vize=int(input("vize notunu giriniz: "))     
    final=int(input("final notunu giriniz: "))    
    ortalama=(vize*0.3)+(final*0.7)
    if ortalama>=50:
        print("geçtiniz Tebrikler ")
    else:
        print("kaldınız. :)")
        
        
    print("devam etmek istiyor musun ? (y/n)")    
    answ=input("cevabınızı giriniz: ")

yas=int(input("lütfen yaşınızı giriniz:"))    

if yas<18:
    print("ehliyet alamazsınız")
else:
    print("ehliyet alabilirsiniz.")
  
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)
    
isim=input("lütfen isminizi giriniz: ")
sayac=0
while  sayac<len(isim):
    print(isim[sayac])
    sayac+=1
    
answer=input("sinema mı tiyatro mu ? ")
ogrenci=input("öğrenci misin(E/H):")
ucret=0

if answer=="sinema":
    ucret=15
elif answer=="tiyatro":
    ucret=10
    
if ogrenci =='E' or ogrenci =='e':
    ucret=ucret/2
    
print("ödemeniz gereken tutar: "+ str(ucret))    











     

