N = 5
for i in range(N):
	for j in range(N):
		if i == j:
			print("#", end="")
		else:
			print("+", end="")
	print()