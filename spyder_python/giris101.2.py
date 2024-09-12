#veri yapıları - tuple 
#kapsayıcıdır-sıralıdır-değiştirilemez 
t=(2,3,4,"sln")
t1= "slen", 23,23,3,3

#tek elemanlı tuplde sonuna virgul koymak gerekir
tuple_=("evrim",)
type(tuple_)

#sozluk - dictionary
sozluk={"reg":"regresyon modeli",
        "loj":"lojistik regresyon",
        "cart":"classification and reg"}
len(sozluk) 
sozluk["reg"]

#eleman ekleme
sozluk["gbm"]="gradient boosting mac"
#eleman degistirme
sozluk["reg"]="coklu deogrusal regresyon"

#set - küme
# =============================================================================
# sırasızdır(indexlenemez)
# degerleri essizdir
# degiştirilebilirdir
# farklı tipleri barındırabilir
# =============================================================================
s=set()
s
l=[1,"a",34]
s=set(l)

ev="evrim_ev_evrim ev"
type(ev)
s=set(ev)
s

s.add("ile")
s

#klasik küme işlemleri
# =============================================================================
# difference() : iki kümenin farkını ya da - ifadesi
# intersection() : iki küme kesişimi ya da & ifadesi
# union() : iki kümenin birleşimi
# symetric_difference() : iki kümede olmayanları 
# =============================================================================

set1=set([1,3,5])
set2=set([1,3,2])

set1.difference(set2)
set2.difference(set1)

set1-set2
set2-set1

set1.symmetric_difference(set2)

set1.intersection(set2)

set1&set2

set1.union(set2)

# ikili kumenin kesisiminin bos olup olmadıgının sorgulanması
set1.isdisjoint(set2)

#bir kumenin butun elemanlarının baska bir kume icerisinde yer alıp almadıgı
set1.issubset(set2)

#bir kumenin bir diger kumeyi kapsayıp kapsamadıgı
set2.issuperset(set1)

















