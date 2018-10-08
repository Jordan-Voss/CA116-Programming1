import sys
pattern = sys.argv[1]
replacement = sys.argv[2]

s = raw_input()
while s != 'END':
   t = ''

   i = 0
   while i < len(s):
      j = i
      while j < len(s) and s[j:j+len(pattern)] != pattern:
         j = j + 1
      t = t +s[i:j]
      i = j

      if i < len(s):
         t = t + replacement
         i = j + len(pattern)
   print t
   s = raw_input()