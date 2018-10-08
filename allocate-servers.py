prev = raw_input()
curr = 0
a = []
while str(curr) != 'end' or str(prev) != 'end':
	a.append(prev)
	if (int(prev) + 1000) >= int(curr) and (int(curr) - int(prev)) < 1000:
		a.append(curr)
	tmp = curr
	prev = curr
	curr = raw_input()
print len(a)