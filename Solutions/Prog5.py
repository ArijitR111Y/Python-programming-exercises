class InputandOutput(object):
	def __init__(self):
		self.str = ""

	def getString(self):
		self.str = input()

	def printString(self):
		print (self.str.upper())
		

def main():
	obj_str = InputandOutput()
	obj_str.getString()
	obj_str.printString()

if __name__ == '__main__':
	main()