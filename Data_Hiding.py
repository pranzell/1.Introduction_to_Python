
class XYZ:

	__emp = 0;								#  PRIVATE MEMBER
	open_var = "Its a PUBLIC variable";

	def __init__(self,n,a):
		self.name = n;
		self.age = a;
		return;

	def func1(self):
		self.__emp +=1;
		print "No. %d  :- Name = %s  Age = %d" % (self.__emp, self.name, self.age);
		return;


obj1 = XYZ("Pranjal", 24);
obj2 = XYZ("Anand", 29);
obj3 = XYZ("Phani", 32);
obj4 = XYZ("Banu", 25);

obj1.func1();
obj2.func1();
obj3.func1();
obj4.func1();

print obj1.open_var;		#  PUBLIC  -  Access directly
print obj1._XYZ__emp;		#  PRIVATE -  Use object._ClassName__PrivateMember;	
