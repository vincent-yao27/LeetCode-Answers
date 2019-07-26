def dailyTemperatures(T):
	stack = []
	result = [0] * len(T)
	for i, t in enumerate(T):
		while stack and T[stack[-1]] < t:
			result[stack[-1]] = i - stack[-1]
			stack.pop()
		stack.append(i)
	return result
