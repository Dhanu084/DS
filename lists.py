lst = []

lst.append(1)
lst.append(2)
lst.append(3)

# lst.insert(0,0)
lst.insert(-1,4)
lst.pop(0)
lst.remove(3)
print(lst.index(4))
print(lst)

del lst[1]

print(lst)