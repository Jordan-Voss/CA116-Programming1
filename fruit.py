fruit = {
   "apple": True,
   "pair": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}
a = []
import sys
words = sys.stdin.read().split()
i = 0
while i < len(words):
	word = words[i]
	if word in fruit:
		a.append(word)
	i += 1
i = 0
while i < len(a):
	print a[i]
	i += 1

