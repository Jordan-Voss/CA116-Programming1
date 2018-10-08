german = {
'one': 'eins',
'two': 'zwei',
'three': 'drei',
'four': 'vier',
'five': 'funf',
'six':'sechs',
'seven':'sieben',
'eight':'acht',
'nine': 'neun',
'ten': 'zehn'
 }
import sys
eng = sys.stdin.read().split()
i = 0
while i < len(eng):
	english = eng[i]
	print german[english]
	i += 1
	