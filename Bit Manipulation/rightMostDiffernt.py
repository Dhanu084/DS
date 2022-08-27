# right most different bit between 2 numbers
a = 10
b = 14

print(bin(a))
print(bin(b))

mask = counter =1

# while (a&mask) == (b&mask):
#     a >>= 1
#     b >>= 1
#     counter += 1

# efficient -> instead of left shifting a and b we can left shift mask i.e mask * 2

while (a&mask) == (b&mask):
    mask <<= 1
    counter += 1
print(counter)