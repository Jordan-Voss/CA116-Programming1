import sys
s = sys.argv
n = raw_input()
i = 0
while n != 'end':
   i += 1
   j = 0
   if n[i:i + len(s)] == s:
      j = j + 1
   print j
   n = raw_input()