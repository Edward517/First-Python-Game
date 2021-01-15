import random

class Player:
    def __init__(self,name,age,hand):
        hands=["Fist","Scissors","Paper"]
        self.name=name
        self.age=age
        self.hand=hands[hand]

class Hero(Player):
    def __init__(self,name,gender,age,hand):
        super().__init__(name,age,hand)
        self.gender = gender
    def info(self):
        return self.name+"  Comes to the stage!"

class Enemy(Player):
    pass

computerhand = random.randint(0,2)
herohand= random.randint(0,2)
Edward=Hero("Edward","male",29,herohand)
Jasmine=Hero("Jasmine","female",25,1)
Computer=Enemy("Computer",9999,computerhand)
Heroes=[Edward,Jasmine]
Enemies=[Computer]

def Heroprinthand(player):

    print(player.name+",Who is "+str(player.age)+"-Year-old, used a powerful  "+player.hand+"!")

def Enemyprinthand(player):

    print("The evil "+player.name+",Who is "+str(player.age)+"-Year-old, used a powerful  "+player.hand+"!")

def judge(playerhand,computerhand):
    if playerhand == 0 and computerhand == 0:
        return "Tied!"
    elif playerhand == 0 and computerhand == 1:
        return "You won!"
    elif playerhand == 0 and computerhand == 2:
        return "You lost!"
    elif playerhand == 1 and computerhand == 0:
        return "You lost!"
    elif playerhand == 1 and computerhand == 1:
        return "Tied!"   
    elif playerhand == 1 and computerhand == 2:
        return "You Won!"  
    else:
        return "To be judged"

print("Let's start the game!")
print("Please select your Hero, 0.Edward/1.Jasmine")
playernumber = int(input("Choose by number"))
Selectedplayer = Heroes[playernumber]

print(Hero.info(Selectedplayer))
Heroprinthand(Selectedplayer)
Enemyprinthand(Computer)

result = judge(Selectedplayer.hand,Computer.hand)
print(result)