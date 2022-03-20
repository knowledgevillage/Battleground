a=12
b=3


print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)



print()


for i in range(1,4):
    print(i)



print()

"""
for i in range(1,a/b):          # TypeError: 'float' object cannot be interpreted as an integer
    print(i)
"""

for i in range(1,a//b):
    print(i)