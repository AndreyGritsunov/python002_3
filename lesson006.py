n = str.lower(input("Введите строку 1: "))
m = str.lower(input("Введите строку 2: "))
coll = 0
for i in n.split(): 
    if i == m: 
        coll = coll + 1 
print (coll)