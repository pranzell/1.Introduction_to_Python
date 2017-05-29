def sum(*a):
	print "-------------- \n SUM";
	my_sum=0;
	for x in a:
		my_sum+=my_sum+x;

	print "OLD *a is  ", a;
	print "Sum is = %d " % (my_sum);
	return;

def power(tup):
	print "-------------- \n POWER";
	my_list = [];

	for x in tup:
		my_list.append(x**2);

	new_tup = tuple(my_list);

	print "OLD Tuple is  ", tup;
	print new_tup;
	return;

def power3(tup):
	print "-------------- \n POWER CUBE";
	my_list = list(tup);

	for i in range(len(my_list)):
		my_list[i] = my_list[i]**3;

	new_tup = tuple(my_list);

	print "OLD Tuple is  ", tup;
	print new_tup;
	return;
