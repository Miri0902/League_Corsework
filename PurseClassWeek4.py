# load money onto the purse
# spend the money in the purse
# transfer all money from some other purse
# query the purse to get balance and last time it was used

class Purse:  # define the class
    ''' A class Purse with money in it'''
    def __init__(self): # the constructor
        self.money = 0

    def load_money(self, amount):  # saying to it to add money
        self.money += amount

    def spend_money(self, amount):
        if amount <= self.money:
            self.money -= amount
        else:
            raise ValueError("Insufficient funds in the purse")
    def balance(self):
        return self.money




