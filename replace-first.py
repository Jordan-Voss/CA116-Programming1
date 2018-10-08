import sys

pat = sys.argv[1]
rep = sys.argv[2]
n = raw_input()

while n != 'end':
   i = 0
   while i < len(n) and pat != n[i:i + len(pat)]:
      i += 1

   if i < len(n):
      print n[:i] + rep + n[i+len(pat):]
   else:
      print n
   n = raw_input()