class Player:
	def __init__(self,name,age,height):
		self.age=age
		self.name=name
		self.height=height

	def IncreaseAge(self):
		self.age+=1

	def PrintInformation(self):
		print("This is {0}, he is {1} years old and {2} cm.".format(self.name,self.age,self.height))


player1=Player("Jhon",20,170)
player1.IncreaseAge()
player1.PrintInformation()
