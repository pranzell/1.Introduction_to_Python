
inp = raw_input("Enter your word -  ");

c=1;

for i in range(len(inp)/2):
	if( inp[i] != inp[len(inp)-i-1]):
		c=0;
		break;

if(c==1):
	print "Plaindrrome";
else:
	print "NOOOOOOO!!";


