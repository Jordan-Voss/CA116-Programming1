import sys
with open(sys.argv[1]) as f:
   s = f.read()
with open(sys.argv[2]) as f:
   t = f.read()
count = 0
pos = 0

i = 0
while i < len(s) and i < len(t) and s[i] == t[i]:
   if s[i] == '\n':
      count += 1
      pos = i + 1
   i += 1
if i < len(s) or i < len(t):
   print count, i - pos