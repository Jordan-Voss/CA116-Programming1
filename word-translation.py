import sys
eng = sys.stdin.read().split()
dic = {}
i = 0
with open('translation.txt') as f:
	f = f.read().split()
	while i < len(f):
		key = f[i]
		if key not in dic:
			dic[key] = f[i + 1]
		i += 2
i = 0
while i < len(eng):
	english = eng[i]
	print dic[english]
	i += 1




	
