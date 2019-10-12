class Card(object):
    name = ""
    value = 0
    secondValue = 0
    position = 0
    def make_card(self, name, value, secondValue):
        self.name = name
        self.value = value
        self.secondValue = secondValue
        # Note: I didn't need to create a variable in the class definition before doing this.
        return self