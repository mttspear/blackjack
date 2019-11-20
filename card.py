class Card(object):
    name = ""
    id = 0
    value = 0
    secondValue = 0
    position = 0
    suit = ""
    image = ""
    imagedir = "cards"
    def make_card(self, name, id, value, secondValue, suit):
        self.name = name
        self.id = id
        self.value = value
        self.secondValue = secondValue
        self.image = self.imagedir + "/" + name + "_of_" + suit + ".png"
        self.suit = suit
        # Note: I didn't need to create a variable in the class definition before doing this.
        return self