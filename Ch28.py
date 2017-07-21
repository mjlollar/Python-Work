#! Python

# Walkthrough with notes on Chapter 28 of Learning Python, 5th

class Person:
	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self):
		return self.name.split()[-1]   # Assumption two names
	def giveRaise(self, percent):
		self.pay = int(slef.pay * (1 + percent))
	def __repr__(self):
		return '[Person: %s, %s]' % (self.name, self.pay)
		
class Manager(Person):
	def giveRaise(self, percent, bonus=0.10):
		Person.giveRaise(self, percent + bonus)
		
		
# Self test

if __name__ == '__main__':
	bob = Person('Bob Smith')
	sue = Person('Sue Jones, job='dev', pay=100000)
	tom = Manager('Tom Jones', 'mgr', 50000)
	tom.GiveRaise(0.10)
	print(bob)
	print(sue)
	print(tom.lastName())
	print(tom)
