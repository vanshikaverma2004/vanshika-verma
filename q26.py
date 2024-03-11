n = 10
result = list(map(lambda x: 2**x, range(n)))

print("The total terms are:", n)
for i in range(n):
    print("2 raise to power", i, "is", result[i])