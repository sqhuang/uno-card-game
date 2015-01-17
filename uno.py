import math
import random
from player import player
from game import game
from card import card
from deck import deck
    
#This function is ugly and hacky and wrong and hopefully ill fix it someday
#Currently only displays the first 5 cards
def printCards(cardGroup):
    sets = math.floor(len(cardGroup) / 5)
    extraCards = len(cardGroup) % 5
    
    def printFunction(start,end):
        lines = dict.fromkeys(["line0","line1", "line2", "line3","line4","line5","line6","line7"], "")

        for x in range(start,int(end)):
            card = cardGroup[x]
            n,c,a = "","",""

            if card.type != "action":
                n = str(card.number)
            else:
                a = card.action

            if card.action != "draw4":
                c = card.color


            lines["line0"] += "------------ "
            lines["line1"] += "|%s" % (n) + (" " * (10 - (len(str(n)) * 2)))  + "%s|" % (n) + " "
            lines["line2"] += "|          | "
            lines["line3"] += "|  %s" % (c) + (" " * (8 - (len(str(c)))))  + "|" + " "
            lines["line4"] += "|  %s" % (a) + (" " * (8 - (len(str(a)))))  + "|" + " "
            lines["line5"] += "|          | "
            lines["line6"] += "|%s" % (n) + (" " * (10 - (len(str(n)) * 2)))  + "%s|" % (n) + " " 
            lines["line7"] += "------------ "
        
        for x in range(0,8):
            print lines["line"+str(x)] + "\r"
    if sets > 0:
        for x in range(0,int(sets)*5,5):
            printFunction(x,(x + 5))
    if extraCards > 0:
        printFunction(int((5 * sets)),(5 * sets) + extraCards)
        
myGame = game(4)
printCards(myGame.getCurrentCard())
print ("Current Hand: ")
printCards(myGame.players[0].getHand())