#nesne yönelimli programlama 



#sınıf ozellikleri
class veriBilimci():
    bolum=''
    sql='evet'
    deneyim_yili=0
    bildigi_diller=[]

veriBilimci.sql  
veriBilimci.sql="hayir" 
veriBilimci.sql  
#sınıf örneklendirmesi(instantiation)
ali=veriBilimci()
ali.sql    
ali.bildigi_diller.append("python")#bu yapılan değişiklik tüm sınıfın özelliklerine eklenir

ali.bildigi_diller
#örnek özellikleri
class veriBilimci():
   bildigi_diller=["R","python"]
   def __init__(self):
       self.bildigi_diller=[]
       self.bolum=''
#yukarıdaki gibi tanımlayarak sadece kişiye özel ekleme sağlar

#örnek methodları
class veriBilimci():
   calisanlar=[]
   def __init__(self):
       self.bildigi_diller=[]
       self.bolum=''
   def dil_ekle(self,yeni_dil):
       self.bildigi_diller.append(yeni_dil)
ali=veriBilimci()      
ali.bildigi_diller
ali.bolum

veli=veriBilimci()
veli.bildigi_diller
veli.bolum

ali.dil_ekle("R")
ali.bildigi_diller

#miras yapıları (inheritance )

class Employees():
    def __init__(self):
        self.FirstName=""
        self.LastName=""
        self.Address=""

class DataSciene(Employees):
    def __init__(self):
        self.Programming=""
          
class Marketing(Employees):
    def __init__(self):
        self.StoryTelling=""

veribilimci1=DataSciene()    

        








    

