import sys
words = sys.stdin.read().split()
dic = {}
a = []
i = 0
while i < len(words) and words[i] not in dic:
	dic[words[i]] = None
	i += 1
if i < len(words):
	print dic