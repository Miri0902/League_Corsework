# tallies hold a internal count, initially 0
# they can be incrented (inc) or decremented (dec)
# and queried to obtain current count (function tally)

class Tally:  # define the class
    ''' A class Tally will obtain count '''
    def __init__(self): # the constructor
        self.count = 0

    def inc(self):
        self.count += 1

    def dec(self):
        self.count -= 1

    def tally(self):
        return self.count


# first define the t as t = Tally(). then to do the increment t.inc(), to call the count t.tall()


# tally harder
# a tally has an optional upper limit
# increments and decrements can be by a certain amount (1 by default - incBy and decBy
# bounded tallies mustn't go beyond the upper limit
# tallies may be reset - count set to 0


