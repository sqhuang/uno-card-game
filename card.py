class card():
    def __init__(self,color,number):
        self.color = color
        self.number = number
        self.action = False
        self.type = ""
    
    #The string representation of each card changes based on whether its color and number matter
    def __repr__(self):
        if self.action == False:
            return '[%s %s]' % (self.color, self.number)
        elif self.action != "draw4":
            return '[%s %s]' % (self.color, self.action)
        else:
            return '[%s]' % (self.action)