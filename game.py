from deck import deck
from card import card
from player import player

class game():
    def __init__(self,playerCount):
        print ("Starting Game...")
        self.deck = deck()
        
        #If the game has a bunch of people, we need more cards, so we creat a double deck
        if playerCount >= 4:
            deck2 = deck()
            self.deck.cards.extend(deck2.cards)
        
        #Once we have all the cards, we shuffle them
        self.deck.shuffle()
        print ("Starting Deck Length: "+str(self.getDeckLength()))
        
        #Time to create players
        self.players = []
        for x in range(0,playerCount):
            print ("Loading Player "+str(x)+"...")
            
            #Draw 5 cards for each player and insert them into our player list
            newPlayerHand = self.deck.drawCard(13)
            newPlayer = player(self,x,newPlayerHand)
            self.players.append(newPlayer)
        
        #We pick a starting card with onlyNumerical = true so we dont start with an action card
        self.currentCard = self.deck.drawCard(1,True)
        print "Current Play Card: " + str(self.getCurrentCard())
        
    #Get Deck Size/Remaining cards in deck
    def getDeckLength(self):
        return len(self.deck.cards)
    
    #Get the current play card
    def getCurrentCard(self):
        return self.currentCard
    
    #Try to play a card
    def playCard(self,card):
        if card.number == self.getCurrentCard().number or card.color == self.getCurrentCard().color:
            self.currentCard[0] = card
            return True
        else:
            return False