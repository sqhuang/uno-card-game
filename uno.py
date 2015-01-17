from player import player
from game import game
from card import card
from deck import deck
from utils import printCards    

        
myGame = game(4)
printCards(myGame.getCurrentCard())
print ("Current Hand: ")
printCards(myGame.players[0].getHand())
myGame.players[0].playCard(0)
print ("Current Player: "+str(myGame.getCurrentPlayer()))