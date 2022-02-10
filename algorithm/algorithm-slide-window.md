## 滑窗法

滑动窗口算法的思路是这样：
1、我们在字符串 S 中使用双指针中的左右指针技巧，初始化 left = right = 0，把索引闭区间 [left, right] 称为一个「窗口」。
2、我们先不断地增加 right 指针扩大窗口 [left, right]，直到窗口中的字符串符合要求（包含了 T 中的所有字符）。
3、此时，我们停止增加 right，转而不断增加 left 指针缩小窗口 [left, right]，直到窗口中的字符串不再符合要求（不包含 T 中的所有字符了）。同时，每次增加 left，我们都要更新一轮结果。
4、重复第 2 和第 3 步，直到 right 到达字符串 S 的尽头。


伪代码：
```

string s, t;
// 在 s 中寻找 t 的「最小覆盖子串」
int left = 0, right = 0;
string res = s;

while(right < s.size()) {
    window.add(s[right]);
    right++;
    // 如果符合要求，移动 left 缩小窗口
    while (window 符合要求) {
        // 如果这个窗口的子串更短，则更新 res
        res = minLen(res, window);
        window.remove(s[left]);
        left++;
    }
}
return res;

```

￼ ￼
### 经典问题

#### 最小覆盖子串

给你一个字符串 S、一个字符串T，请在字符串S 里面找出：包含下所有字母的最小子串。

示例：
- 输入：s="ADOBECODEBANC". T = "ABC"
- 输出:  "BANC"

说明：
- 如果S 中不存这样的子串，则返回空字符串 “”
- 如果S中存在这样的子串，我们保证它是唯一的答案。

```python

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

```
