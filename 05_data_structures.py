# Lists
# Mutable
l = [1, 2, 3, 4, 5]
print(l[0])
l.append(6)
print(l[-1])

# Tuples
# Immutable
t1 = (1, 2, 3, 4, 5)
t2 = (6,)
t3 = t1 + t2
print(t3)
print(len(t3))

# Range
# Generator, exhausts after use.
r = range(10)
for i in r:
	print(i)
for i in r:
	print(i)

# Dictonaries (maps).
d = {'a': 1, 2: 'b'}
print(d['a'])
print(len(d))
