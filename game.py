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
        
        
        #index of current player (players list)
        self.currentPlayer = 0;
        
        #which direction the flow is going
        self.rotationManager = 1
        
    #Get Deck Size/Remaining cards in deck
    def getDeckLength(self):
        return len(self.deck.cards)
    
    #Get the current play card
    def getCurrentCard(self):
        return self.currentCard
    
    #Get number of players in the game
    def getNumPlayers(self):
        return len(self.players)
    
    #Get current player's turn
    def getCurrentPlayer(self):
        return self.currentPlayer
    
    #Forces all players to draw cards except for player who initialized
    #draw2 and draw4
    def drawAll(self,playerIndex,numberOfCards):
        for x in range(0,len(self.players)):
                if x != playerIndex:   
                        self.players[x].deck.drawCard(numberOfCards)
    
    #Skip next player
    def skipCard(self):
        self.nextPlayer()
 
    #reverse queue of rotation
    #We manage the rotation by using a positive/negative 1 integer
    #Every turn, the play() adds 1 * (rotationManager)
    def reversePlay(self):
        #negate rotationManager or bring back to positive
        self.rotationManager *= -1
       
 
    def nextPlayer(self):
        calculatedNextPlayer = self.getCurrentPlayer + (1 * self.rotationManager)
       
        if calculatedNextPlayer < 0:
                calculatedNextPlayer = getNumPlayers()
        elif: calculatedNextPlayer > getNumPlayers()
                calculatedNextPlayer = 0
        else:
                #just a valid pick
       
        self.currentPlayer = calculatedNextPlayer
    #Try to play a card
    def playCard(self,card,index):
        currentCard = self.getCurrentCard()
        if index == self.currentPlayer:
            if card.number == currentCard[0].number or card.color == currentCard[0].color:
                self.currentCard[0] = card
                if index == self.getNumPlayers():
                    self.currentPlayer = 0
                else:
                    self.currentPlayer += 1
                    print ("Played Card!")
                    print ("Current Player's Turn: "+str(self.getCurrentPlayer()))
                    return True
            else:
                print ("Invalid Card")
                return False
        else:
            print ("Wrong player!")
            return False
