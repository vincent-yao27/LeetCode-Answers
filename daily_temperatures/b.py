'''
基于栈，从底到顶按温度从高到低排列
'''


def dailyTemperatures(T):
	stack = []
	result = [0] * len(T)
	for i in range(len(T) - 1, -1, -1):
		while stack and T[i] >= T[stack[-1]]:
			stack.pop()
		if stack:
			result[i] = stack[-1] - i
		stack.append(i)
	return result
