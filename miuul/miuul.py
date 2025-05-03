#data structures

#liste,tuple set ve dictionary veri yapıları aynı zamanda python collections (arrays)olarak geçemktedir.
# üç çift iki tırnak arasına uzun string yazılabilir.

type(len)

#Fonksiyonlar

print("a","b",sep="--")

def calculate(x):
    print(x*2)
    
calculate(5)

def summer(arg1,arg2):
    """
    sum of two number

    Parameters
    ----------
    arg1 : int ,float
        DESCRIPTION.
    arg2 : int float
        DESCRIPTION.

    Returns
    -------
    int,float

    """
    print(arg1+arg2)
summer(12,13) 
#♣Docstring

#fonksiyonların Statement/Body Bölümü

def say_hi():
    print("merhaba")
    print("hi")
    print("hello")

say_hi()   

#girilen değerleri bir liste içinde saklayacak fonksiyon

list_store=[] 
def add_list(a, b):
   c=a*b
   list_store.append(c)
   print(list_store)
    
add_list(8, 9)
#Y ön tanımlı argümanlar/parametreler

def calculate(varm,moisture,charge):
    return (varm+moisture)/charge

calculate(90, 12, 12)

def standardization(a, p):
    return a*10 / 100 * p  *p  

def all_calculation(varm,moisture,charge,p):
    a=calculate(varm, moisture, charge)
    b=standardization(a, p)
    print(int(b*10))

all_calculation(1, 3, 5, 12)

students=["Barıs","İcardi","Osimhen","Lemina"]

for i in students:
    print(i)

for i in students:
    print(i.upper())

strings="hi my name is John and i am learning python"    

def alternating(string):
    new_string = ""
    for i in range((len(string))):
        if i % 2==0:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    print(new_string)         

alternating("strings")    

#enumerate:otomatik counter ile for loop
#4index değerlerini de yazmamaızı sağlar
students= ["John","Mark","Venessa","Mariam"]

for student in students:
    print(student)

for index,student in enumerate(students,1):
    print(index,student)
    
A=[]
B=[]

for index,student in enumerate(students,1):
    if index % 2 == 0:
        A.append(student)
    else:
       B.append(student)

def divide_students(students):
    groups=[ [], []]
    for index,student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups    

divide_students(students)            
    
#alternating fonksiyonunun enumerate ile yazılması

def alternating_with_enumerate(string):
    new_string=""
    for i,letter in enumerate(string):
        if i % 2 ==0:
            new_string+= letter.upper()
        else:
            new_string+=letter.lower()
    print(new_string) 

alternating_with_enumerate("gulveren")

#zip :farklı listeleri bir arada değerlendirme imkanı sağlar 

departments=["math","statistics","physics","astronomy"]

ages=[23,26,30,22]

list(zip(students,departments,ages))

#ön tanımlı argümanlar

def divide(a,b=1):
    print(a/b)
    
divide(5)   

#♣ne zaman fonk yazılır

#warm moisture chaarge

def calculate(warm,moisture,charge):
    print(warm+moisture/charge)

calculate(58,80,5)

#lambda,map,filter ,reduce
def summer(a,b):
    return a+b

new_sum= lambda a,b:a+b
#buda bir fonksiyondur

new_sum(7,5)

#•map:döngü yazmaktan kurtarır

salaries=[1000,2000,3000,4000,5000]

def new_salary(x):
    return x*20/100+x

for salary in salaries:
    print(new_salary((salary)))

list(map(new_salary,salaries))
#fonksiyon ve üzerinde gezinebileceği nesne vererek for yazmaktan kurtulduk

list(map(lambda x:x*20/100+x,salaries))

#fılter 

list_stores=[1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x:x%2==0,list_stores))

#reduce:indirgemek

from functools import reduce

reduce(lambda a,b:a+b,list_stores)


#comprehensions:birden fazla satır ve kodla yapılacak işlemleri kolayca istediğimiz veri yapısına göre tek satırdaa gerçeklerştirir

#list compherension

salaries

[new_salary(salary*2) if salary<3000 else new_salary(salary) for salary in salaries]

students=["john","Mark","Venessa","Mariam"]

students_no=["John","Venessa"]

[  student.lower() if student in students_no  else student.upper() for student in students]

#dict compherension

dictionary={'a':1,
            'b':2,
            'c':3,
            'd':4}
dictionary.keys()
dictionary.values()
dictionary.items()

{k:v**2 for (k,v) in dictionary.items()}

{k.upper():v for (k,v) in dictionary.items()}
    
#Uygulama-Mülakat sorusu

#amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir.
#keyler orjibal değerler value lar değiştirilmiş değerler olacak
numbers=range(10)

new_dict={}

for n in numbers:
    if n%2==0:
        new_dict[n]= n**2

{n:n**2 for n in numbers if n % 2==0}

 #list & dict comprehension uygulamalar 
 
 #1-bir veri setindeki değişken isimlerini değiştirmek
 
import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns
df.columns = [col.upper() for col in df.columns]
df.columns

#isminde "INS" olan değişkenlerin başına FLAG diğerlerine "NO_FLAG" eklemek isityoruz.

[col for col in df.columns if "INS" in col]

[ "FLAG_" + col for col in df.columns if "INS" in col]

["FLAG" + col if "INS" in col else "NO_FLAG_" + col  for col in df.columns]

#amaç:key'i string,value'su aşağıdaki gibi bir liste olan sözlük oluşturmak
#sadece sayısal değişkneler için bunu yapmak istiyoruz
df.columns

num_cols = [col for col in df.columns if df[col].dtype !="O"]

soz={}
agg_list=["mean","min","max","sum"]

for col in num_cols:
    soz[col] = agg_list
new_dict=soz

df[num_cols].agg(new_dict)
