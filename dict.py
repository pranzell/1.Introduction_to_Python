
dict = { "Name" : "Pranjal", "Age" : 23, "Sex" : "Male", "Height" : 5.11 };


for x in dict:
	print x;			#KKey

	print dict[x];		#Values


print "------------";


for key,value in dict.items():
	print key, " = ", value;