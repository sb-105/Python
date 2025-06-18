#understanding datattypes
print(type(2))
print(type(14.62))
print(type("SVR"))
print(type(3+4J))
print(type([1,'q',2.4]))#list is a combination of any datattype
print(type((1,2,3.2)))#tuple
print(type({1,2,3}))#sets are mutable
print(type({1:23,'a':34.5,1:"abc"}))#dictionary
print(type(frozenset({1,2,3})))
'''frozenset is immutable version of set,once defined it cant be changed,but however it still supports most set operations like union,inteersections...
why frozenset insted of set--->
1)you want to protect the data from being modified
2)you want a set that can be hashable(can be used a dictionary key or set element)'''
print(type(True))
