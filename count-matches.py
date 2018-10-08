import sys
pattern = sys.argv[1]
line = raw_input()
while line != "end":
   count = 0
   i = 0
   while i < len(line):
      while i < len(line) and line[i:i+len(pattern)] != pattern:
         i = i + 1
      if i < len(line):
         count = count + 1
         i = i + len(pattern)
   print count
   line = raw_input()