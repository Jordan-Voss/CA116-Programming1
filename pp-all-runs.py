import sys
s = sys.argv[1] 
i = 0
while i < len(s):
   j = i                            
   while j < len(s) and s[j] == s[i]: 
      j = j + 1

   print s[i], j - i
   i = j