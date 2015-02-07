
class Player:
        def __init__(self,name,age,height):
                self.age=age
                self.name=name
                self.height=height

        def IncreaseAge(self):
                self.age+=1

        def PrintInformation(self):
                print(self.name,self.age,self.height)


class Team(Player):
	def __init__(self,name,country,plist):
		self.name=name
		self.country=country
		self.plist=plist
		self.win=0

	def AddPlayer(self,player):
		self.plist.append(player);
		print("join {0}.".format(player.name))

	def RemovePlayer(self,name):
		for player in self.plist:
			if(player.name == name):
				self.plist.remove(player);
				print("remove {0}.".format(player.name))

	def CountVictories(self):
		self.win=+1

	def PrintInformation(self):
		print("This Team is {0}, It from {1} and {2} win.Team member is as follow.".format(self.name,self.country,self.win))
		for player in self.plist:
			print("{0}: ({1} years old , {2} cm.)".format(player.name,player.age,player.height))


player1=Player("Jhon",20,170)
player1.IncreaseAge()
player2=Player("Anna",18,156)
player3=Player("Taro",22,182)
player4=Player("Ken",19,172)
player5=Player("Jessica",20,165)

list=[player1,player2,player3,player4,player5]
team=Team("Tea","Japan",list)
team.PrintInformation()
player6=Player("Adora",23,175)
team.AddPlayer(player6)
team.RemovePlayer("Taro")
team.CountVictories()
team.PrintInformation()
