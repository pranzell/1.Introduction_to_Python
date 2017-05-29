s = "The quick brown fox jumps over the lazy dog";


""" ---LONGER METHOD -- 

s = s.upper();
print s;

for j in range(65,91):
	alpha = chr(j);
	c=0;
	
	for i in s:
		if(alpha==i):
			c=1;
			break;

	if(c!=1):
		print "Not a panagram";
		break;

if(c==1):
	print "YEPPP!!!"
"""

""" SMALLER METHOD """

s = "".join(str(x) for x in s.split());

s = s.lower();

l = len( set(s) );		# -> set(x) :  Collection of all unique elements in a string/list/etc x. 

if(l==26):
	print "Panagram";
else:
	print "NOO";