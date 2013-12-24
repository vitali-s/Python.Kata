class Game(object):
    def __init__(self):
        self.rolls = []

    def Roll(self, number):
        self.rolls.append(number)

    def Score(self):
        rolls = 0
        score = 0
        frameScore = 0

        for index, value in enumerate(self.rolls):
            rolls += 1
            frameScore += value
            score += value

            if rolls == 1 and frameScore == 10:
                if index + 1 < len(self.rolls):
                    score += self.rolls[index + 1]

                if index + 2 < len(self.rolls):
                    score += self.rolls[index + 2]

                rolls = 0
                frameScore = 0

            if rolls == 2:
                if frameScore == 10:
                    score += self.rolls[index + 1]

                rolls = 0
                frameScore = 0

        return score