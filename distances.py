import sys
lines = sys.stdin.readlines()

distances = {}
i = 0
while i < len(lineS):
	tokens = lines[i].split()
	src = tokens[0] + '-' + tokens[1]
	dst = tokens[1] + '-' + tokens[0]
	dist = int(tokens[2])
	distances[src] = dist
	distances[dst] = dist
	i += 1
total = 0	
i = 2 
while i < len(sys.argv):
	key = sys.argv[i - 1] + '-' + sys.argv[i]
	total = total + distances[key]
	i += 1
print total