for i in range(10):
    print(i)

a = [1, 2, 3, 4]

for i in a:  # Iterable
    print(i)

a = (1, 2, 3, 4)

for i in a:  # Iterable
    print(i)

f = open("foo.txt")

for i in f:  # Iterable
    print(i)

x = 12
for i in x:  # NOT Iterable, you can't "iterate" over a single object...
    print(i)
