dic = {}
n = raw_input()
while n != 'end':
	n = n.split()
	dic[n[0]] =n[1:]
	n = raw_input()
n = raw_input()
while n != 'end':
	print dic[n]
	n = raw_input()
