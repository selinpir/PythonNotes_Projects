print("hello ai era")
type("hello ai era")
type("123")
type(11)
type(1+2j) #complex
" a"*3

# metod len()
a= "atama"
b= "9"
sp="absslfkjfosjfo" 
len(sp)

#upper()& lower()
c="Evrim Alasya"
c.upper()
c.lower()

#isupper()& islower()
p="malaka"
p.isupper()
p.islower()

#replace
r="take away"
r.replace("away","go")

#strip(kırpma)
s="udemy"
s.strip("u")

#dir (kullanılabilecek metodları gösterir)
g="gelecegi yazanlar"
dir(g)
g.title()
g.swapcase()

#substring
g[0] #index
g[0:3]

#type_donusumleri
birinci_sayi=input()
ikinci_sayi=input()
#yukaridaki iki sayiyi da string olarak aldı matematiksel işlem yapamayız.

#numerik anlamda toplayabilmek için başına int,float vb. koyulmalı.
int(birinci_sayi)+int(ikinci_sayi)

11.0
int(11.0)

12
float(12)

str(12)

type(str(12))

#print sep kullanım
print("hello","ai","era",sep="_")
#? ilgili seyin dokumanını acar
#?int

"""
VERİ YAPILARI
LİSTELER
   *degistirilebilirdir
   *kapsayıcıdır-farklı tipte veri tutabilir
   *sıralıdır
"""
#[]
#list()

notlar=[90,80,70,60]
type(notlar)

liste=["é",19,90.01]
liste_genis=[12,12,23,notlar]
 
del liste[2]
dir(liste)

#append : listeye eleman ekleme
liste.append("selin")
#remove : listeden elaman kaldırma
liste.remove("é")
#insert : listeye eleman ekleme
liste.insert(0,"evrim")
#listenin SONUNA eleman ekleme
liste.insert(len(liste),"kıvılcım")
#pop : listeden eleman silme
liste.pop(1)

#count()
liste=[1,1,1,2,3,4,5,6,6,6,6,7,7,0]
liste.count(1)

#copy()
liste_yedek=liste.copy()

#extend()
liste.extend(["a","b",10])
liste

#index()
liste.index(1)

#reverse()
liste.reverse()
liste

#sort()
liste_ee=[10,29,280,129]
liste_ee.sort()
liste_ee

#clear()
liste.clear()

