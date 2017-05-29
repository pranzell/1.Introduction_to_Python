
#This File.py contains 2 classes:

class Employee_Details:

	def __init__(self,name,age,sex,emp_no):
		self.name=name;
		self.age=age;
		self.sex=sex;
		self.emp_no=emp_no;

	def func(self,salary,band):
		self.salary = salary;
		self.band = band;

	def printer(self):
		print "Name = ", self.name;
		print "Age = ", self.age;
		print "Sex = ", self.sex;
		print "Emp NO = ", self.emp_no;
		print "Salary = ", self.salary;
		print "Band = ", self.band;
		
class Employee_Position:

	def __init__(self,loc,unit):
		self.loc = loc;
		self.unit=unit;

	def account(self,acc_name):
		self.account_name = acc_name;

	def pp(self):
		print "Account is = ", self.account_name;
		print "Location and unit are = ", self.loc, self.unit;