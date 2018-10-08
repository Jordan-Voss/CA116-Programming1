import sys
i = 0
boys = {}
girls = {}
either = {}
with open('boys.txt') as boy:
	b = boy.read().split()
	while i < len(b) and b[i] not in boys:
		boys[b[i]] = 'boy'
		i += 1
j = 0
with open('girls.txt') as girl:
	g = girl.read().split()
	while j < len(g):
		if g[j] not in girls:
			girls[g[j]] = 'girl'
		j += 1
i = 0 
while i < len(g):
	if g[i] in boys and g[i] in girls:
		either[g[i]] = 'either'
	i += 1


x = sys.stdin.read().split()
i = 0
while i < len(x):
	if x[i] in either:
		print x[i],either[x[i]]
		i += 1
	elif x[i] in boys:
		print x[i], boys[x[i]]
		i += 1
	elif x[i] in girls:
		print x[i], girls[x[i]]
		i += 1
