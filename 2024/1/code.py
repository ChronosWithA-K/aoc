from collections import Counter

a, b = [], []

with open ('2024/1/input.txt', 'r') as f:
    for line in f.readlines():
        x, y = (int(z) for z in line.split())

        a.append(x)
        b.append(y)

a.sort()
b.sort()

l = len(a)
print("part 1 solution")
print(sum(abs(a[i] - b[i]) for i in range(l)))

c = Counter(b)
print("part 2 solution")
print(sum(a[i] * c[a[i]] for i in range(l)))
