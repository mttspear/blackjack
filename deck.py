# pylint: disable=no-member
from card import Card
from pprint import pprint
from random import randint
import random

class Deck:
    cards = {'two': {'name': '2',
                    'value': 2,
                    'secondValue': None},
            'three': {'name': '3',
                    'value': 3,
                    'secondValue': None},
            'four': {'name': '4',
                    'value': 4,
                    'secondValue': None},
            'five': {'name': '5',
                    'value': 5,
                    'secondValue': None},
            'six': {'name': '6',
                    'value': 6,
                    'secondValue': None},
            'seven': {'name': '7',
                    'value': 7,
                    'secondValue': None},
            'eight': {'name': '8',
                    'value': 8,
                    'secondValue': None},
            'nine': {'name': '9',
                    'value': 9,
                    'secondValue': None},
            'ten': {'name': '10',
                    'value': 10,
                    'secondValue': None},
            'jack': {'name': 'jack',
                    'value': 10,
                    'secondValue': None},
            'queen': {'name': 'queen',
                    'value': 10,
                    'secondValue': None},
            'king': {'name': 'king',
                    'value': 10,
                    'secondValue': None},
            'ace': {'name': 'ace',
                    'value': 11,
                    'secondValue': 1},
            }
    suits = ['hearts', 'clubs', 'spades', 'diamonds']
    fullDeck =[]
    cardCount = 4
    deckCount = 1
    cardsDeck = 52
    def __init__(self, deckCount):
        self.deckCount = deckCount
        deckTotal = self.cardCount * self.deckCount
        i = 1
        for suit in self.suits:
            for card in self.cards:
                name = self.cards[card]['name']
                cardObj = Card()
                cardObj.make_card(name,i, 11,1, suit)
                self.fullDeck.append(cardObj)
                i+= 1
  

    def shuffelDeck(self):
        random.shuffle(self.fullDeck)

