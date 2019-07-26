'''
根据观察发现所求解即为 K-1 的奇偶校验 (Parity Check)
'''


def kthGrammar(self, N: int, K: int) -> int:
	# just a parity check algorithm that I don't understand
	K -= 1
	K ^= K >> 1
	K ^= K >> 2
	K = (K & 0x11111111) * 0x11111111
	return (K >> 28) & 1
