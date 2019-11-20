class CardCounter(object):
    deckRemaining = 0
    runningCount = 0
    trueCount = 0
    changeAmmount = 0  

    def setCount(self, card, deckRemaining):
        self.deckRemaining =  deckRemaining
        if card.value >= 2 and card.value <= 6:
            self.runningCount += 1
        elif card.value >= 7 and card.value <= 9:
            self.runningCount += 0
        elif card.value >= 10:
            self.runningCount -= 1

        self.trueCount = float(self.runningCount / self.deckRemaining)
        #print 'cardValue:' + str(card.value) + 'runningCount:' + str(self.runningCount) + 'trueCount:' + str(self.trueCount)

    def getWager(self, wager, baseWager):
        newWager = 0
        if self.trueCount <= -4:
           newWager =  baseWager * 5
        elif self.trueCount >= 2 :
            newWager =  baseWager / 10
        else:
            newWager = baseWager
        return newWager
            
        