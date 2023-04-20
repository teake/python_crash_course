x = -1
y = 3

assert x.__bool__() == bool(x)
assert x.__add__(y) == x + y
assert x.__hash__() == hash(x)
assert x.__class__ == type(x)
