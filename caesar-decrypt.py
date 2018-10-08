import sys
sentence = sys.stdin.read()
w = 'nopqrstuvwxyzabcdefghijklm'
x = 'abcdefghijklmnopqrstuvwxyz'
y = 'NOPQRSTUVWXYZABCDEFGHIJKLM'
z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c = ' '
b = '.'
d = '\n'
e = ','
a = []
i = 0
dic = {}
while i < 26:
	dic[w[i]] = x[i]
	dic[y[i]] = z[i]
	i += 1
i = 0
while i < len(sentence):
	if sentence[i].isupper() or sentence[i].islower():
		a.append(dic[sentence[i]])
	else:
		a.append(sentence[i])
	i += 1
n = ''.join(a)
print n,

