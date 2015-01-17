from player import player
from game import game
from card import card
from deck import deck
from utils import printCards    

class commandHandler():
    def __init__(self,game):
        self.game = game
        self.setup()
        
    def setup(self):
        print ("Type !uno for options")
        userInput = input("Enter Command: ")
        commands = ["!uno","!player","!game","!exit"]
        userInput = userInput.split(" ")
        
        if userInput[0] == commands[0]:
            self.unoCommands()
        elif userInput[0] == commands[1]:
            self.playerAction(userInput)
        elif userInput[0] == commands[2]:
            self.gameAction(userInput)
        elif userInput[0] == commands[3]:
            print ("Bye")
        else:
            print ("Not valid command!")
            self.setup()
    
    def unoCommands(self):
        print ("----COMMANDS------------------")
        print ("!player <index> [play,getHand,draw] [cardIndex,null,numberOfCards]")
        print ("!game [getCurrentCard,getPlayers,getCurrentPlayer] @aliases [GCC,GP,GCP]")
        print ("!exit")
        print ("------------------------------")

    def playerAction(self,userInput):
        commands = ["play","getHand","draw"]
        player = int(userInput[1])
        number = int(userInput[3])
        
        if userInput[2] == commands[0]:
            if isinstance(number,int):
                self.game.players[player].playCard(number)
                printCards(myGame.players[player].getHand())
                self.setup()
                
        elif userInput[2] == commands[1]:
            printCards(self.game.players[player].getHand())
            self.setup()
            
        elif userInput[2] == commands[2]:
            if isinstance(number,int):
                self.game.players[player].drawCard(number)
        else:
            print ("Not valid command!")
            self.setup()
        

myGame = game(4)
print ("Current Player: "+str(myGame.getCurrentPlayer()))
print ("------------------------------")
print ("Current Play Card: ")
printCards(myGame.getCurrentCard())
print ("------------------------------")
print ("Player 0's hand: ")
printCards(myGame.players[0].getHand())

commandHandler(myGame)
