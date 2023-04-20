l = list(range(10))

squared = [i*i for i in l]
cubed = [i*i*i for i in l]

for s in squared:
	print(s)

d = {i: i*i for i in l}
for k, v in d.items():
	print(k, v)
