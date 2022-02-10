from collections import Counter


class MinString(object):
	
	def __init__(self, source, target):
		self.t = dict(Counter(target))
		self.s = source
	
	def is_valid(self, sstr):
		sc = dict(Counter(sstr))
		for k, v in self.t.items():
			if k in sc and sc[k] >= v:
				pass
			else:
				return False
		
		return True 
		
	
	def run(self):
		left = right = 0
		res = self.s
		MAX_LEN = len(self.s)
		while (right <= MAX_LEN):
			sub_str = self.s[left:right]
			right += 1
			print(1, sub_str)
			while self.is_valid(sub_str):
				if len(sub_str) < len(res):
					res = sub_str
				sub_str = sub_str[1:]
				print(2, sub_str)
				left += 1
		
		return res
	
	
res = MinString('ADOBECODEBANC', 'ABC').run()
print('res: ', res)