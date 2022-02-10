"""
实现全排列：
inputs：
	nums: numbers need to be ordered
	
"""

res = []

def permute(nums, path):
    print(path)
    if len(path) == len(nums):
        res.append(tuple(path))
        return
   
    for i, n in enumerate(nums):
        if n in path:
            continue
        path.append(n)
        permute(nums, path)
        path.pop()


permute([1,2,3], [])

print("res: ", res)