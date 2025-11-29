a = {"apple":120,"orange":200}
a["grapes"]= 200
print(a)
print(a.get("apple")) #return value
del a["orange"]
a["strawberry"] = 300
print(a)
print(list(a))
a["banana"] = 100
print(sorted(a))


a= dict(sape=4139, guido=4127, jack=4098)
print(a)