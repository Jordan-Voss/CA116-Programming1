line = raw_input()
while line != 'end':

   i = 0 
   while i < len(line) and line[i] != '+':
      i += 1
   i += 1

   j = i
   while j < len(line) and line[j] != '+':
      j += 1

   if j < len(line):
      text = line[i:j]

      if 4 <= len(text) and text[len(text)-3:] == '.py':
         print text

   line = raw_input()