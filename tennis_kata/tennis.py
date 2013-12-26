class Tennis(object):
    def __init__(self):
        self.playerOne = 0
        self.playerTwo = 0

    def player_one_win(self):
        self.playerOne += 15

    def player_two_win(self):
        self.playerTwo += 15

    def score(self):
        return "{0} - {1}".format(self.playerOne, self.playerTwo)