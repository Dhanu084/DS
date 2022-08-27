# Find right most bit efficiently
'''
Right most bit the right most 1 for any binary number
eg for 4 (0 1 0 0) the right most bit is at the 3rd position
TimeComplexity : O log2N
'''
mask = 1
n = int(input())
print(f'The binary representation is {bin(n)}')
counter = 1

# while n:
#     if n & mask == 1:
#         break
#     counter+=1
#     n>>=1
# print(counter)

while n & mask == 0:
    counter+=1
    n>>=1
print(counter)

'''
4 - 0 1 0 0
1 - 0 0 0 1

0 1 0 0
0 0 0 1 doing &
0 0 0 0
counter = 2

right shift n by 1
0 0 1 0
0 0 0 1 doing &
0 0 0 0
counter = 3

right shift n by 1
0 0 0 1
0 0 0 1
now we get 1 at the end and we return counter
'''