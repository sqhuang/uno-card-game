class player():
    def __init__(self,game,playerNumber,hand):
        self.playerNumber = playerNumber
        self.hand = hand
        self.playerGame = game
        
    def playCard(self,cardIndex):
        if self.playerGame.playCard(self.hand[cardIndex],self.playerNumber):
            self.hand.pop(cardIndex)
            return True
        else:
            return False
        
    #Uno attack mode is a random draw of cards when a user needs a new card
    #They randomly get between 0 and 5 cards every draw when enabled
    def drawCard(self,number=None,unoAttackMode=None):
        if unoAttackMode is None:
            unoAttackMode = False
        
        if number is None:
            number = 1
        
        if unoAttackMode == True:
            number = int(math.floor(random.random() * 5))
            print ("Uno attack mode!!")
            
        self.hand.extend(self.playerGame.deck.drawCard(number))
        
    def getHand(self):
        return self.hand
        
    def __repr__(self):
        return 'Player %s has cards %s' % (self.playerNumber,self.hand)
