from card import Card
from pprint import pprint
from random import randint
import random

class Deck(object):
 	fullDeck =[]
	cardCount = 4
	deckCount = 1
	cardsDeck = 52
	totalCards = 0

	def __init__(self, deckCount):
    		self.deckCount = deckCount
		deckTotal = self.cardCount * self.deckCount
		for count in xrange(deckTotal):
			aceCard = Card()
			twoCard = Card()
			threeCard = Card()
			fourCard = Card()
			fiveCard = Card()
			sixCard = Card()
			sevenCard = Card()
			eightCard = Card()
			nineCard = Card()
			tenCard = Card()
			jackCard = Card()
			queenCard = Card()
			kingCard = Card()
			aceCard.make_card('ace',11,1)
			twoCard.make_card('two',2,None)
			threeCard.make_card('three',3,None)
			fourCard.make_card('four',4,None)
			fiveCard.make_card('five',5,None)
			sixCard.make_card('six',6,None)
			sevenCard.make_card('seven',7,None)
			eightCard.make_card('eight',8,None)
			nineCard.make_card('nine',9,None)
			tenCard.make_card('ten',10,None)
			jackCard.make_card('jack',10,None)
			queenCard.make_card('queen',10,None)
			kingCard.make_card('king',10,None)
			self.fullDeck.append(aceCard)
			self.fullDeck.append(twoCard)
			self.fullDeck.append(threeCard)
			self.fullDeck.append(fourCard)
			self.fullDeck.append(fiveCard)
			self.fullDeck.append(sevenCard)
			self.fullDeck.append(eightCard)
			self.fullDeck.append(nineCard)
			self.fullDeck.append(tenCard)
			self.fullDeck.append(jackCard)
			self.fullDeck.append(queenCard)
			self.fullDeck.append(kingCard)
			
	def shuffelDeck(self):
		positionArray = []
		i = 0
		maxPosition = self.cardsDeck * self.deckCount
		self.totalCards = maxPosition
		data = range(1, maxPosition)
		random.shuffle(data)
		for sel in self.fullDeck :
			sel.position = data[i]
			i +=1
		self.fullDeck.sort(key=lambda dec: dec.position)
		for sel in self.fullDeck :
				name = "%s and %s"%(sel.name,sel.position)