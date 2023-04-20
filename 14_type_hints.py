x: str = 'Hello'
y: int = 1

def fibonacci(n: int) -> int:
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

fibonacci("foobar")
