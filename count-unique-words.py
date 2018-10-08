import sys
words = sys.stdin.read().split()
counts = {}
i = 0 
while i < len(words):
	word = words[i]
	if word not in counts:
		counts[word] = 0
	counts[word] += 1
	i += 1

for word in counts:
	if counts[word] == 1:
		print word
	
