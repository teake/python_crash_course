def fibonacci(n):
	"""Fibonacci number."""
	if not isinstance(n, int):
		raise TypeError(f"Expected positive int, got {n} ({type(n)})")
	if n < 0:
		raise ValueError(f"Expected postive int, got {n}") 
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
	print(fibonacci(i))

try:
	fibonacci("foobar")
except Exception as e:
	print(e)


def say_hi(first_name=None, last_name=None):
	if first_name is None:
		first_name = "John"
	if last_name is None:
		last_name = "Doe"
	msg = f"Hi, {first_name} {last_name}!"
	print(msg)

say_hi(first_name="Peter")
