"""
high level support for doing this and that.
"""
from pprint import pprint

class BlackjackStrategy(object):
    action = "Hit"
    cardSum = 0
    nonAceSum = 0
    cards = []
    dealerUpcard = 0
    aceInHand = False
    cardCount = 0
    softTotalAction = False

    
    def getCardTotal(self):
        self.setCardCount()
        for card in self.cards:
            pprint(card.value)
            self.cardSum += card.value
            # Check for ace
            if card.secondValue != None:
                self.aceInHand = True
                self.nonAceSum += card.secondValue
            else:
                self.nonAceSum += card.value
        #If Ace and count less then 21
        if self.cardSum < 21 and self.aceInHand is True:
            self.softTotalAction = True
        #if over 21 and have an ace use the ace as single
        if self.cardSum > 21 and self.aceInHand is True:
            self.cardSum =  self.nonAceSum
            
    #set the card count
    def setCardCount(self):
        self.cardCount =  len(self.cards)

    #get dealer action
    def getDealerAction(self):
        self.getCardTotal()
        if self.cardSum < 17:
            self.action = 'Hit'
        elif self.cardSum > 21:
            self.action = 'Bust'
        else:
            self.action = 'Stand'
    #get player decision
    def getAction(self, dealerUpcard):
        pprint("cardSum" +  str(self.cardSum ))
        #get card total
        self.getCardTotal()
        self.dealerUpcard = dealerUpcard.value
        #If over 21 Bust
        if self.cardSum > 21:
            self.action = 'Bust'
        #if Card Count 2 and Total 21 BlackJack
        elif self.cardCount == 2 and self.cardSum == 21:
            self.action = 'Blackjack'
        #If under 21 and ace
        elif self.softTotalAction == True:
            self.softTotals()
        else:
            self.hardTotals()

    def softTotals(self):
        if self.nonAceSum == 9:
            self.action = 'Stand'
        elif self.nonAceSum == 8:
            self.action = ''
        elif self.nonAceSum == 7 and self.dealerUpcard  <=8:
            self.action = 'Stand'
        elif self.nonAceSum == 6 and self.dealerUpcard  <=6:
            self.action = 'Hit'
        else:
            self.action = 'Hit'

    def hardTotals(self):
        #Greater then 17
        if self.cardSum >= 17:
            self.action = 'Stand'
        # Greater then 13 and dealer upcard less than 7
        elif self.cardSum >= 13 and self.dealerUpcard  <= 6:
            self.action = 'Stand'
        elif self.cardSum >= 12 and self.dealerUpcard  >=4  and self.dealerUpcard  <= 6:
            self.action = 'Stand'
        #return self.action

    def checkSame(self):
        if self.cards[0].name == self.cards[1].name:
            return True
        else:
            return False

    def checkSplit (self, dealerUpCard):
        if self.cards[0].name == 'Ace':
            return True
        elif self.cards[0].value == 9 and dealerUpCard.value !=7 and dealerUpCard.value <= 9 :
            return True
        elif self.cards[0].name == 8 :
            return True
        elif self.cards[0].name == 7 and dealerUpCard.value <= 7 :
            return True
        elif self.cards[0].name == 6 and dealerUpCard.value <= 6 :  
            return True   
        elif self.cards[0].name == 4 and dealerUpCard.value >=5 and  dealerUpCard.value <=6 :  
            return True  
        elif self.cards[0].name == 3 and dealerUpCard.value <=7 :
            return True    
        elif self.cards[0].name == 2 and dealerUpCard.value <=7 :      
            return True 
        else:
            return False
            
