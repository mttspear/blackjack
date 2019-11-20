from tkinter import *  
from PIL import ImageTk,Image 
from blackjack import Blackjack  
from pprint import pprint
import time

class Interface(object):
    players = {'house': {
                'xcord': 300,
                'ycord': 50,
                'nextXCord': 300,
                'nextYCord': 50,
                'type' : 'dealer',
                'lableXCord': 320,
                'lableYCord': 20,
                'balanceXCord': 320,
                'balanceYCord': 220,
                
                },
            'player1': {
                'xcord': 100,
                'ycord': 300,
                'nextXCord': 100,
                'nextYCord': 300,
                'type' : 'dealer',
                'lableXCord': 120,
                'lableYCord': 280,
                'balanceXCord': 120,
                'balanceYCord': 480,
                },
            'computer': {
                'xcord': 500,
                'ycord': 300,
                'nextXCord': 500,
                'nextYCord': 300,
                'type' : 'dealer',
                'lableXCord': 520,
                'lableYCord': 280,
                'balanceXCord': 520,
                'balanceYCord': 480,
                }
            }
    runCount={}
    images={}
    deckImage={}
    valueLable=[]
    playerLable=['balance:', 'wager:', 'status:', 'score:']
    deckLable=['decks:', 'used:', 'remaining:']
    fontColor="darkblue"
    fontStyleLarge="Times 20 italic bold"
    fontStyleSmall="Times 14 bold"

    def __init__(self):
        self.bj = Blackjack()
        self.root = Tk()  
        self.canvas = Canvas(self.root, width = 900, height = 600)  
        self.canvas.pack() 
        self.canvas.configure(background='green')
        self.addInputs()
        self.addButtons()
        self.addLables()
        self.addDeck()
        self.root.mainloop() 

    def playGame(self):
        #runCount = int(self.runCount.get())
        #pprint(runCount)
        #i = 0
        self.dealCards()
        time.sleep(1) 
        self.playHand()
        time.sleep(1) 
        self.scoreHand()
        self.root.mainloop() 
        time.sleep(1) 
        self.dealCards()
        time.sleep(1) 
        self.playHand()
        time.sleep(1) 
        self.scoreHand()
        time.sleep(1) 

    def dealCards(self):
        self.bj.deal()
        self.images = {}
        self.resetPlayerCords()
        for player in self.bj.gamePlayers:
            for card in player.cards:
                self.showCard(player, card)

    def playHand(self):
        self.bj.playerAction()
        for player in self.bj.gamePlayers:
            for card in player.cards:
                if card.id not in self.images:
                    self.showCard(player, card)

    def scoreHand(self):
        self.clearCounts()
        self.bj.scoreHands()
        for player in self.bj.gamePlayers:
            self.updateCounts(player)

    def showCard(self, player, card):
        xcord = self.players[player.name]['nextXCord']
        ycord = self.players[player.name]['nextYCord']
        uid = card.id
        self.players[player.name]['nextXCord'] = xcord + 20
        self.images[uid] = Image.open(card.image)  
        self.images[uid] = self.images[uid].resize((100, 145), Image.ANTIALIAS)   
        self.images[uid] = ImageTk.PhotoImage(self.images[uid])
        self.canvas.create_image(xcord, ycord, anchor=NW, image=self.images[uid]) 

    def resetPlayerCords(self):
        for player in self.players:
            #pprint(self.players[player])
            self.players[player]['nextXCord'] = self.players[player]['xcord']
            self.players[player]['nextYCord'] = self.players[player]['ycord']

    def updateCounts(self, bjplayer):
        xcord = self.players[bjplayer.name]['balanceXCord'] + 100
        ycord = self.players[bjplayer.name]['balanceYCord']
        id = self.canvas.create_text(xcord,ycord,fill=self.fontColor,font=self.fontStyleSmall,text=bjplayer.balance)
        self.valueLable.append(id)
        ycord=ycord+20
        id = self.canvas.create_text(xcord,ycord,fill=self.fontColor,font=self.fontStyleSmall,text=bjplayer.wager)
        self.valueLable.append(id)
        ycord=ycord+20
        scoreId = self.canvas.create_text(xcord,ycord,fill=self.fontColor,font=self.fontStyleSmall,text=bjplayer.cardTotal)
        self.valueLable.append(scoreId)
        ycord=ycord+20
        id = self.canvas.create_text(xcord,ycord,fill=self.fontColor,font=self.fontStyleSmall,text=bjplayer.playerStatus)
        self.valueLable.append(id)

    def clearCounts(self):
         for textId in self.valueLable:
             #pprint(textId)
             self.canvas.delete(textId)

    def addLables(self):
        for player in self.players:
            xcord = self.players[player]['lableXCord']
            ycord = self.players[player]['lableYCord']
            self.canvas.create_text(xcord,ycord,fill=self.fontColor,font=self.fontStyleLarge,text=player)
            xcord = self.players[player]['balanceXCord']
            ycord = self.players[player]['balanceYCord']

            for text in self.playerLable:
                self.canvas.create_text(xcord,ycord,fill=self.fontColor,font=self.fontStyleSmall,text=text)
                ycord=ycord+20

    def addButtons(self):
        btn2 = Button(self.root, text = 'Play',  command = self.playGame)
        btn2.pack(side = 'top') 

    def addDeck(self):
        xcord = 700
        ycord = 50
        self.deckImage = Image.open('cards/deck.png')  
        self.deckImage = self.deckImage.resize((100, 145), Image.ANTIALIAS)   
        self.deckImage = ImageTk.PhotoImage(self.deckImage)
        self.canvas.create_image(xcord, ycord, anchor=NW, image=self.deckImage) 
        self.addDeckLables()

    def addDeckLables(self):
        xcord = 750
        ycord = 210
        for text in self.deckLable:
            self.canvas.create_text(xcord,ycord,fill=self.fontColor,font=self.fontStyleSmall,text=text)
            ycord=ycord+20

    def addInputs(self):
        a = Label(self.root , text="Run Count")
        a.pack(side = 'top')
        self.runCount = Entry(self.root )
        self.runCount.pack(side = 'top')

Interface = Interface() 
