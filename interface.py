from tkinter import *  
from PIL import ImageTk,Image 
from blackjack import Blackjack  
from pprint import pprint

class Interface(object):
    players = {'house': {'xcord': 300,
                'ycord': 50,
                'nextXCord': 300,
                'nextYCord': 50,},
            'player1': {'xcord': 100,
                'ycord': 300,
                'nextXCord': 100,
                'nextYCord': 300,},
            'computer': {'xcord': 500,
                'ycord': 300,
                'nextXCord': 500,
                'nextYCord': 300,}
                }
    images={}
    def __init__(self):
        self.bj = Blackjack()
        self.root = Tk()  
        self.canvas = Canvas(self.root, width = 900, height = 600)  
        self.canvas.pack() 
        self.canvas.configure(background='green')
        btn = Button(self.root, text = 'Deal', 
                          command = self.showCards)
        btn.pack(side = 'top')  
        self.showCards()
        self.root.mainloop() 

    def showCards(self):
        self.bj.deal()
        self.images = {}
        self.resetPlayerCords()
        for player in self.bj.gamePlayers:
            for card in player.cards:
                self.showCard(player, card)
                pprint(self.players[player.name]['nextXCord'])


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
            pprint(self.players[player])
            self.players[player]['nextXCord'] = self.players[player]['xcord']
            self.players[player]['nextYCord'] = self.players[player]['ycord']

    def showCounts(self):
        self.canvas.create_text(400,25,fill="darkblue",font="Times 20 italic bold",
                                text="Dealer")

Interface = Interface() 
