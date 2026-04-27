import timeit
import random

def search():
    for x, y in test:
        binary_search(0, x)

def binary_search(left, right):
    if left > right:
        return None

    mid = (left + right) // 2
    if mid + y == x:
        return mid
    elif mid + y < x:
        return binary_search(mid + 1, right)
    else:
        return binary_search(left, mid - 1)

test = []
for _ in range(4000):
    x = random.randint(10, 1000)
    y = random.randint(1, x - 1)
    test.append((x, y))

x, y = test[1]
z = binary_search(0, x)
print((z+y)-x)

print(timeit.timeit(search, number=1))