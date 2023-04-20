def almost_equal(x, y, delta=0.001):
	return abs(x-y) <= delta

assert almost_equal(1, 1.0)

def almost_equal_wrapper(*args, **kwargs):
	print(args)
	print(kwargs)
	return almost_equal(*args, **kwargs)

assert almost_equal_wrapper(1, 2, delta=3)
