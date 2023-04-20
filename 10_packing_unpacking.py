t = (1, 2, 3)

x, y, z = t
print(x, y, z)

x, *y = t
print(x, y)

t2 = (*t, 4, 5, 6)
print(t2)
