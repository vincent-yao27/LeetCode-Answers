'''
倒序判断
- 当今天温度大于昨天时，结果为1
- 否则，记与昨天进行比较的日期为D（即i+days），D初始为比今天温度高的日期（即今天的结果），若D温度高于昨天，则结果为到D的天数，否则更新D为比D温度高的日期，再次比较。
'''


def dailyTemperatures(T):
	max_t = T[-1]  # max temperature
	result = [0] * len(T)
	for i in range(len(T) - 1, 0, -1):
		if T[i - 1] >= max_t:
			result[i - 1] = 0
			max_t = T[i - 1]
		elif T[i] > T[i - 1]:
			result[i - 1] = 1
		else:
			days = result[i]  # from today to the day to be compared with yesterday
			while i + days < len(T):
				if T[i + days] > T[i - 1]:
					result[i - 1] = days + 1
					break
				days += result[i + days] or 1
			else:
				raise Exception('Not found')
	return result
