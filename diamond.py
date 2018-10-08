import sys
s = sys.argv[1]
spaces = (int(s) - 1) / 2
middle = int(s)
i = 1
while i < middle:
	print ' ' * spaces + '*' * i
	i += 2
	spaces = spaces - 1

print '*' * middle

spaces = spaces + 1
i = (middle - 2)
while i > 0:
	print ' ' * spaces + '*' * i
	i -= 2
	spaces = spaces + 1