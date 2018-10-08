import sys
s = sys.stdin.readline()
total = 0
while 0 < len(s):
   total = total + int(s)
   s = sys.stdin.readline()
print total