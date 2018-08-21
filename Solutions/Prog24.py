class Employee(object):
	"""docstring for Employee"""
	def __init__(self, fname, lname, pay):
		self.fname = fname
		self.lname = lname
		self.pay = pay
	def update_pay(self, new_pay):
		self.pay = new_pay
	def print_details(self):
		print ('Name: {} {} has a salary of just {}'.format(self.fname, self.lname, self.pay))

emp1 = Employee('Arijit', 'Roy', 200)
emp1.print_details()