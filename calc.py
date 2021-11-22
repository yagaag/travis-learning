def calculate(v1, v2, op):
	if op == '+':
		return v1 + v2
	elif op == '-':
		return v1 - v2
	elif op == '*':
		return v1 * v2
	elif op == '/':
		return v1 / v2
	else:
		return v1

print(calculate(5, 6, '-'))
