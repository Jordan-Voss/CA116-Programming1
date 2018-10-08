import sys
 
s = sys.argv[1]
d = sys.argv[2]
if len(s) < 5:
   s = '0' + s            
if len(d) < 5:
   d = '0' + d            
sh = int(s[:2])           
sm = int(s[3:])           
 
dh = int(d[:2])           
dm = int(d[3:])           
 
s = 60 * sh + sm          
d = 60 * dh + dm       
e = (s + d) % (24 * 60)
eh = e / 60 
em = e % 60 
if em < 10:
   em = '0' + str(em)
print str(eh) + ":" + str(em)