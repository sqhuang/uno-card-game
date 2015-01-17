from card import card
import math
import random

class deck():
    def __init__(self):
        #Assign new deck
        self.cards = self.newDeck()
        
    def newDeck(self):
        #Deck placeholder + possible colors and actions
        newDeck = []
        colors = ["blue","red","green","yellow"]
        actions = ["draw2","draw4","reverse","skip"]
    
        #For all colors
        for color in colors:
            #Make numerical cards 1-9
            for x in range(0,10):
                newCard = card(color,x)
                newCard.type = "number"
                newDeck.append(newCard)
            
            #Make action cards 10-13, with specified action
            for x in range(0,4):
                newCard = card(color,x+10)
                newCard.type = "action"
                newCard.action = actions[x]
                newDeck.append(newCard)
        
        return newDeck
    
    def shuffle(self):
        #Fisher-Yates shuffle 
        for x in range (len(self.cards) - 1,0,-1):
            select = int (math.floor(random.random() * (x + 1)))
            temp = self.cards[x]
            self.cards[x] = self.cards[select]
            self.cards[select] = temp
            
    def drawCard(self,numberOfCards,numericalCardsOnly=None):
        #Default parameter value
        if numericalCardsOnly is None:
            numericalCardsOnly = False
            
        cards = []
        while numberOfCards > 0:
            #We randomly pick a card
            select = int(math.floor(random.random() * len(self.cards)))
            card = self.cards[select]            
                
            #If we only want numerical cards, we make sure the card's type is number
            if numericalCardsOnly == True:
                if card.type == "number":
                    cards.append(card)
                    self.cards.pop(select)
                    numberOfCards -= 1
            else:
                #If its false, we dont care what card it is so every picked card is valid
                cards.append(card)
                self.cards.pop(select)
                numberOfCards -= 1
        
        return cards