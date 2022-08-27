n = 4
k = 1
mask = 1

while k>1:
    mask<<=1
    k-=1

print(mask & n != 0)