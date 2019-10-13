from blackjackStrategy import BlackjackStrategy

class Player(object):
    name = ""
    playerType = ""
    seatPosition = 0
    wager = 100
    baseWager = 100
    balance = 0
    cards = []
    cardTotal = 0
    aceInHand = False
    playerStatus = ""
    playerSplit = False
    cardCounter = None
    playerCards = []
               
    def getPlayerStatus(self, dealerCard):  
        blackjackStrategy = BlackjackStrategy()
        blackjackStrategy.cards =  self.cards
        #if Dealer do dealer status
        if self.playerType != 'dealer': 
            blackjackStrategy.getAction(dealerCard)
        else:
            blackjackStrategy.getDealerAction()
        self.playerStatus = blackjackStrategy.action
        self.cardTotal = blackjackStrategy.cardSum

    def checkSplit(self, dealerUpCard):
        blackjackStrategy = BlackjackStrategy()
        blackjackStrategy.cards =  self.cards
        if blackjackStrategy.checkSame():
            return blackjackStrategy.checkSplit(dealerUpCard)
        else:
            return False

        
        
        
