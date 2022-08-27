n = 4
l = 1
r = 3

print(bin(n))
mask = 1
i = 1
power = value = 0

while i<l: # include all bits before the flip range
    if mask & n:
        value+=pow(2,power)
    mask<<=1
    power+=1
    i+=1

while i<=r:
    if not mask & n: # if value is 1 we do not add it because we are anyways toggling it to 0 so add only 1
        value+=pow(2, power)
    power+=1
    mask<<=1
    i+=1

while i<=10: # include all renaining bits
    if mask & n:
        value+=pow(2, power)
    power+=1
    mask<<=1
    i+=1

print(value, bin(value))