class player():
    def __init__(self,game,playerNumber,hand):
        self.playerNumber = playerNumber
        self.hand = hand
        self.playerGame = game
        
    def playCard(self,cardIndex):
        if self.playerGame.playCard(self.hand[cardIndex]):
            self.hand.pop(cardIndex)
            print ("Played Card!")
            return True
        else:
            print ("Invalid Card Choice")
            return False
        
    def drawCard(self):
        self.hand.extend(self.playerGame.deck.drawCard(1))
        
    def getHand(self):
        return self.hand
        
    def __repr__(self):
        return 'Player %s has cards %s' % (self.playerNumber,self.hand)
