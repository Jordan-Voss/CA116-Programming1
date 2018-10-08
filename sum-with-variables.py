import sys 
lines = sys.stdin.readlines()
assign = {}
process = []
total = 0
i = 0
while i < len(lines):
	line = lines[i].rstrip().lstrip()
	if line.isdigit():
		total = total + int(line)
	elif line[0] == "-":
		total = total + int(line)
	else:
		j = 0
		while j < len(line) and line[j] != "=":
			j = j + 1
		if j < len(line):
			variable = line[ : j].rstrip()
			integer = line[j + 1: ].rstrip().lstrip()
			assign[variable] = int(integer)
		else:
			variable = line[ : j].rstrip().lstrip()
			total = total + assign[variable]
	i = i + 1
print total