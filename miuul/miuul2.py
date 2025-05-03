import numpy as np
#numpy arrayi oluÅŸturmak

np.array([1,2,3,4,5])
type(np.array([1,2,3,4,5]))

np.zeros(10,dtype=int)

np.random.randint(0,10,size=10)

np.random.normal(10,4,(3,4))

#numpy array Ã¶zellikleri

#ndim:boyut sayÄ±sÄ±
#shape:boyut bilgisi
#size: toplam eleman sayÄ±sÄ±
#dtype:array veri tipi

a= np.random.randint(10,size=5)
a.ndim
a.shape
a.size
a.dtype

#reshaping

np.random.randint(1,10,size=9)

np.random.randint(1,10,size=9).reshape(3,3)

#index seÃ§imi

b= np.random.randint(10,size=10)

b[0]
b[0:5]

#Fancy index

v= np.arange(0,30,3)

catch=[1,2,3]

v[catch]
#numpyda koÅŸullu iÅŸlemler

v=np.array([1,2,3,4,5])

#klasik dÃ¶ngÃ¼ ile

ab=[]

for i in v:
    if i < 3:
        ab.append(i)

#numpy ile

v<3

v[v<3]

#matematiksel iÅŸlemlet
v
v/5
v*5/10

#PANDAS

#pandas serileri

import pandas as pd

s=pd.Series([10,7,45,4,5])

s.index

s.dtype

df = pd.read_csv("C:\\Users\\gulveren\\planets.csv")

df.head()

import seaborn as sns

df= sns.load_dataset("titanic")

df.head()

df.tail()
df.shape
df.info()

df.describe().T


df.isnull().values.any()

df.isnull().sum()

df["sex"].value_counts()

df.index

df.drop(0,axis=0).head()
#df.drop(0,axis=0,inplace=True) bu şekilde değişiklik kalıcı hale gelir

#değişkeni indexe çevirmek

df.index = df["age"]

df.drop("age",axis=1,inplace=True)
df.head()

#☺indexi değişkene çevirmeü

df["age"]= df.index
df.head()

#2.yol

df=df.reset_index()
df.head()

#☻bir data frame de bir değişkenin varlıpını sorgulama

"age" in df

df["age"].head()


df[["age","alive"]]

#değişken ekleme

df["age2"]= df["age"]**2

df.drop("age2",axis=1).head()
#belirli bir string ifadeyi içerenleri sil
df.loc[:,~df.columns.str.contains("age")].head()


#iloc & loc

#iloc:integer based selection

df.iloc[0:3]#bu 0 1 2 yi alır

#♥loc :label based selection
df.loc[0:3]# bu 0 1 2 3 ü alır

#koşullu seçim 

df[df["age"]>50].head()
df[df["age"]>50]["age"].count()

df.loc[df["age"]>50,"class"].head()

df.loc[df["age"]>50,"class"].head()

df.loc[(df["age"]>50) & (df["sex"]== "male"),["age","class"]].head()

#toplulaştırma ve gruplama

#count()-first()-last()-mean()-median()-min()-max()-std()

df["age"].mean()
#cinsiyete  göre ortakmayı öğrenmek istiyorum

df.groupby("sex")["age"].mean()

df.groupby("sex").agg({"age":"mean"})

df.groupby("sex").agg({"age":["mean","sum"]})


df.groupby("sex").agg({"age":["mean","sum"],
                       "survived":"count"})


df.groupby(["sex","embark_town"]).agg({"age":["mean","sum"],
                       "survived":"mean"})

#Pivot table

import pandas as pd
import seaborn as sns
df=sns.load_dataset("titanic")
df.head()

df.pivot_table("survived","sex","embarked")
#kesişim satır sütün kesişimin otomatik ortalamasını alır istersen değiştirebilirsin

df.pivot_table("survived","sex","embarked",aggfunc="std")

df.pivot_table("survived","sex","embarked",aggfunc="std")

df.pivot_table("survived","sex",["embarked","class"])

# age değişkenini sayısal değişkenden kategorik değişkene çevirdim çünkü pivotta kullanmak için
df["new_age"]=pd.cut(df["age"],[0,10,18,25,40,90])

df.pivot_table("survived","sex","new_age")

#apply & lambda 

df["age2"]=df["age"]*2
df["age3"] = df["age"]*5

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())
        
#yukarıdaki aynı işlemi şimdi apply ve lambda ile uygulayacağız

df[["age","age2","age3"]].apply(lambda x:x**2).head()      

df.loc[:,df.columns.str.contains("age")].apply(lambda x: x/10).head()


#birleştirme (join işlemleri)
import numpy as np

m = np.random.randint(1,30,size=(5,3))

df1=pd.DataFrame(m,columns =["var1","var2","var3"])

df2=df1+99

pd.concat([df1,df2],ignore_index=True)

#merge ile birleştirme işlemleri

df1=pd.DataFrame({"employees":['John','dennis','mark','maria'],
                   'group':['accounting','engineering','enginnering','hr']})

df2= pd.DataFrame({'employees':['mark','john','dennis','maria'],
                   'start_date':[2010,2009,2014,2019]})

pd.merge(df1, df2 ,on="employees")














