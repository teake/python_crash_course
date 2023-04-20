class Person:

	def __init__(self, first_name, last_name):
		if not first_name:
			first_name = "John"
		if not last_name:
			last_name = "Doe"
		self.first_name = first_name
		self.last_name = last_name

	def introduce(self):
		print(self._introduction_message())

	def _introduction_message(self):
		return f"Hi, I'm {self.first_name} {self.last_name}."

	@classmethod
	def from_input(cls):
		first_name = input("First name:")
		last_name = input("Last name:")
		return cls(first_name, last_name)


if __name__ == "__main__":
	p = Person.from_input()
	p.introduce()
