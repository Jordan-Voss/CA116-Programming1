import sys
i = 1
total = 0
while i < len(sys.argv):
	s = sys.argv[i]
	with open(s) as f_in:
		a = f_in.readlines()
		j = 0
		while j < len(a):
			k = 0
			while k < len(a[j].split()):
				total = total + int(a[j].split()[k])
				k += 1

			j += 1
	i += 1
print total
