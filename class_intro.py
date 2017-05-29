
class Enemy:

	life = 3;

	def attack(self):			# 'self' : Used for referring to an Object. 
		print "Oouch";	
		self.life-=1;
		return;

	def check_life(self):
		if self.life <=0:
			print("You Are Dead!");
		else:
			print("Your life left : ", self.life);
		return;


obj1 = Enemy();

obj1.attack();
obj1.check_life();