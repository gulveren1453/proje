#string methodları -len

gel="gelecegi_yazanlar"
#del love
a=9
b=7
a*b
len(gel)#len() kaç elemandan oluştuğunu gösteririr

#upper() & lower()
gel.upper()
B=gel.lower()
gel.islower()#hepsi küçükse true gönderir yoksa false
gel.isupper()
B.isupper()
#replace() methodu stringdei bir harfi başka bir harfe çeviriri
c="-kerem-"
c.replace("e","a")
gel.replace("E", "A")
#strip() stringdeki boşlukları kaldırır
#tırnak içinde stripin içine ne yazarsam onu da kaldırır etrafından
c.strip("-")
#methodlara genel bakış
#dir() içine veri tipini yazdığımızda o veri tipine hangi methodlar uygulana bileceğini konsola yazdırır
dir(c)
#substringler elimizdeki stringlerin alt birimine erişmemizi sağlar
gel[6]
gel[0:3]
#type donusumleri

toplama_bir=input()
toplama_iki=input()

type(toplama_bir)

toplama_bir+toplama_iki
int(toplama_bir)+int(toplama_iki)

7
type(7)
type(str(7))

#PRİNT()

print("gulveren","canpolat")
print("gulveren","canpolat",sep= "-")
#sep= iki ifadeyi ne ile birleştireceğineceğine karar verir


#veri yapıları
#-listeler
#.değiştirilebilir,kapsayıcıdır,sıralıdır
#[] or list()
notlar=[7,99,53,93]
listenew=["a",19.3,90,notlar]#C de tek çeşit barındırırken farklı türleri barındıra biliyor
#liste içine liste tanımlayabilirisn
len(listenew)
type(notlar)
type(listenew[3])
tum_liste=[notlar,listenew]#iki listeyi birleştirdim
#listeler eleman işlemleri
liste=[18,9,1,42]
liste[0:2]
liste[:3]
yeni_liste=["k",10,[50,20,30]]
yeni_liste[2]
yeni_liste[2][2]
#listeler-eleman değiştirme
liste2=["kerem","gülveren","yunis"]
liste2[1]="gülvereninBabası"
liste2
liste2=liste2+["icardi"]
liste2
del liste2[2]
liste2
#listeler-liste methodları
#append methodu listeye eleman eklemeye yarar
liste2.append("barış")
liste2
liste2.remove("barış")
liste2
#insert methodu
liste2.insert(0,"muhammet")
liste2
len(liste2)
liste2.insert(len(liste2),"dayı")
liste2
#pop eleman silmek için kullanılır
liste2.pop(0)
liste2
#count methodu
liste2=["kerem","ali","kerem","veli"]
liste2.count("kerem")
liste_yedek=liste2.copy()
#extend listeye liste ekleme gibi düşün
liste2.extend(["a","b",7])
liste2
#•index yazdığımız verinin hangi stringde olduğunu söyler
liste2.index("kerem")
#reverse elemanları terse çevirir
liste2.reverse()
liste2
#sort listedeki değerleri küçükten büyüğe sıralar
liste=[5,8,99,7,53]
liste.sort()
liste
#sort eğer string veri tipi için kullanılırsa alfabetik sıralama yapar
listel=["aksam","gul","beren"]
listel.sort()
listel
#clear methodu tüm listeyi siler 



#veri yapıları-TUPLE
#listeler değiştirilebilir yapıdadır ama tuplelar değiştirilemez
t=("kerem",1,5,6.5)
type(t)
#►veri yapıları dictinory(sözlük)
#değiştirilebilir
#sırasızdır index işlemi yapılamaz
sozluk={"reg":"regresyon",
        "loj":"lojistik"}
len(sozluk)
#eleman ekleme degistirmek
sozluk["reg"]
sozluk["gul"]="kerem"
sozluk
sozluk["reg"]="rejenerasyon"
sozluk
l=[1]
sozluk[l]="yeni bir sey"
t=(tuple,)
sozluk[t]="yeni bir sey"
sozluk
#göründüğü gibi tuple key olarak atanor ama liste atanmaz

#veri yapıları-Setler
#sırasızdır yani index işlemi yok,değerleri eşsizdir yani tekrar eden veri barındıramaz
#değiştirilebilir
#farklı veri tipleri barındırabilir

#set oluştırma

s=set()

l=[1,"a","ali",123]
s=set(l)

t=("a","ali")
s=set(t)

k=["kerem","topu","dısarı","atma","kerem","topu","kaleye","at","topu"]
s=set(k)
s
#set function tekrar eden değerleri de bir kere yazar
len(s)

#eleman ekleme çıkarma

i=["kerem","icardi"]
s=set(i)
s
s.add("ile")
s
s.remove("icardi")
s

#setler -Klasik lüme işlemleri
# =============================================================================
# difference() ile ikş kümenin farkını yada "-" ifadesi ile
# intersection() iki kume kesisimi ya da & ifadesi ile
# union() iki kümenin birlesimi
# symetric_difference() ikisinde olmaynalrı
# =============================================================================

set1=set([1,2,3])
set2=set([1,2,5])

set1.difference(set2)#♣set 1 de olup 2 de olamyanı yazdırır

set1.symmetric_difference(set2)#ikisinde de olmayan

set1.intersection(set2)#ikisinde ortak olan değerler
set1&set2# aynısı olur

set1=set1.union(set2)#birleşim
set1

#set sorgu işlemleri

set3=set([7,8,9])
set4=set([5,6,7,8,9,10])


#iki kümenim kesişiminin bos olup olamdığının sorgulanamsı

set3.isdisjoint(set4)
#eğer false dönerse kesişen değer var

#bir kümenin butun elemanlarının baska bir kume icerisinde yer alıp almadığı

set3.issubset(set4)














































