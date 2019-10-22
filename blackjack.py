import config as cfg
import copy
from player import Player
from deck import Deck
from cardCounter import CardCounter
from pprint import pprint
from inspect import getmembers
from writeFile import WriteFile

class Blackjack(object):
    deck = []
    cardCounter = CardCounter()
    deckCount = 1
    deckLocation = 1
    gamePlayers = []
    dealerUpCard = 0
    handCount = 0
    shuffelPercent = .50

    def __init__(self):
        self.createPlayers()
        self.createDeck()

    #Play
    def playHand(self):
        self.deal()
        self.playerAction()
        self.scoreHands()
    # Create the Players 
    def createPlayers(self):    
        playerCount = cfg.playerDetail['count']
        players = cfg.players
        for configPlayer in cfg.players :
            p = Player()
            p.name = players[configPlayer]['name']
            p.playerType = players[configPlayer]['playerType']
            p.seatPosition = players[configPlayer]['seatPosition']
            if players[configPlayer]['playerType'] == 'counter':
                p.cardCounter = self.cardCounter
            p.cards = []
            self.gamePlayers.append(p)
        self.gamePlayers.sort(key=lambda dec: dec.seatPosition)
    # Create The Deck        
    def createDeck(self):         
        deck = Deck(self.deckCount)
        deck.shuffelDeck()
        self.deck = deck
    #make wagers 
    def makeWagers(self):
        #make wager
        for player in self.gamePlayers:
            if player.playerType == 'counter':
                player.wager = self.cardCounter.getWager(player.wager, player.baseWager)
    #reset shuffel
    def resetShuffle(self):
        self.deckLocation = 1
        self.deck.shuffelDeck()
        self.cardCounter.trueCount = 0
        self.cardCounter.deckRemaining = 0
        self.cardCounter.runningCount = 0
        
    # Deal    
    def deal(self): 
        #If Deck over X done resuffle
        deckCount = len(self.deck.fullDeck)
        if (self.deckLocation / deckCount) > self.shuffelPercent:
            self.resetShuffle()
        #clear cards
        for gamer in self.gamePlayers:
            gamer.cards = []
            gamer.playerCards = []
        #place your bets
        self.makeWagers()
        cardsDelt = 0
        while cardsDelt < 2:
            for gamer in self.gamePlayers:
                gamer.cards.append(self.deck.fullDeck[self.deckLocation])
                #set the coutn
                deckRemaining = float(self.deckCount - float(self.deckLocation / 52.0))
                self.cardCounter.setCount(self.deck.fullDeck[self.deckLocation], deckRemaining)
                #if gamer is dealer and second card set upcard
                if gamer.playerType == 'dealer' and cardsDelt == 1:
                    self.dealerUpCard = self.deck.fullDeck[self.deckLocation]
                self.deckLocation += 1
            cardsDelt += 1
        #add hands to player hands
        for gamer in self.gamePlayers:
             gamer.playerCards.append(gamer.cards)
    # Player Action
    def playerAction(self):
        for gamer in self.gamePlayers:
            #check split
            if gamer.checkSplit(self.dealerUpCard):
                #if split make second hand
                secondCard = [gamer.playerCards[0][1]]
                gamer.playerCards.append(secondCard)
                del gamer.playerCards[0][1]
                #hit each hand
                gamer.playerCards[0].append(self.deck.fullDeck[self.deckLocation])
                self.deckLocation +=1
                gamer.playerCards[1].append(self.deck.fullDeck[self.deckLocation])
                self.deckLocation +=1
            #play the hands
            for hand in gamer.playerCards:
                gamer.getPlayerStatus(self.dealerUpCard)
                pprint(gamer.name + gamer.playerStatus)
                while gamer.playerStatus == 'Hit':
                    gamer.cards.append(self.deck.fullDeck[self.deckLocation])
                    self.deckLocation +=1
                    pprint("deckLoc:"+str(self.deckLocation))
                    gamer.getPlayerStatus(self.dealerUpCard)
    # Evaluate Hands
    def scoreHands(self):
        game = 'Tie'
        #get dealer value
        for idx, gamer in enumerate(player for player in self.gamePlayers):
            if gamer.playerType == "dealer":
                dealerIndex = idx 
                dealerHand = gamer.cardTotal
        for gamer in [player for player in self.gamePlayers if player.playerType != "dealer"]:
            #Player Bust
            if gamer.playerStatus == 'Bust':
                game = 'player bust'
                gamer.balance -= gamer.wager
                self.gamePlayers[dealerIndex].balance  += gamer.wager
            #Black Jack 21
            elif gamer.playerStatus == 'Blackjack':
                game = 'blackjack'
                gamer.balance += (gamer.wager * 2)
                self.gamePlayers[dealerIndex].balance -= (gamer.wager * 2)
            #If Player  Doesn't Bust but Dealer Does
            elif self.gamePlayers[dealerIndex].playerStatus == 'Bust':
                game = 'dealer bust'
                gamer.balance += gamer.wager 
                self.gamePlayers[dealerIndex].balance  -= gamer.wager
            #Player Wins
            elif gamer.cardTotal >  dealerHand:
                game = 'player wins'
                gamer.balance += gamer.wager 
                self.gamePlayers[dealerIndex].balance  -= gamer.wager
            #Dealer Wins
            elif gamer.cardTotal <  dealerHand:
                game =  'dealer wins'
                gamer.balance  = (gamer.balance - gamer.wager) 
                self.gamePlayers[dealerIndex].balance  += gamer.wager
            #logg
            cards = ''
            dealerCards = ''
            for card in gamer.cards:
                cards += str(card.name) + ' '
            for card in self.gamePlayers[dealerIndex].cards:
                dealerCards += str(card.name) + ' '
            writeFile = WriteFile()

            remianingCards = ''
            deckLocation = self.deckLocation
            deckCount = len(self.deck.fullDeck)
            while deckLocation < deckCount:
                remianingCards += ',' + self.deck.fullDeck[deckLocation].name
                deckLocation += 1
            gameArray = [game,dealerHand, dealerCards, gamer.name, str(gamer.cardTotal), cards, gamer.wager, gamer.balance, self.cardCounter.runningCount, self.cardCounter.deckRemaining, str(self.cardCounter.trueCount), str(remianingCards)]
            writeFile.logData(gameArray)
            game = 'Tie'