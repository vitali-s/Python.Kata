import unittest


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


class MyTestCase(unittest.TestCase):

    def test_score_forZeroRoll_shouldReturnZero(self):
        game = Game()
        game.Roll(0)

        for index in range(0, 19):
            game.Roll(0)

        score = game.Score()

        self.assertEqual(score, 0)

    def test_score_forPositiveRoll_shouldReturnValue(self):
        game = Game()
        game.Roll(2)

        for index in range(0, 19):
            game.Roll(0)

        score = game.Score()

        self.assertEqual(score, 2)

    def test_score_forSpareRoll_shouldReturnValueWithDoubledNextRoll(self):
        game = Game()
        game.Roll(4)
        game.Roll(6)
        game.Roll(7)

        for index in range(0, 17):
            game.Roll(0)

        score = game.Score()

        self.assertEqual(score, 24)

    def test_score_forStrikeRoll_shouldReturnValueWithDoubledNextTwoRolls(self):
        game = Game()
        game.Roll(10)
        game.Roll(4)
        game.Roll(5)

        for index in range(0, 16):
            game.Roll(0)

        score = game.Score()

        self.assertEqual(score, 28)

    def test_score_forAllStrikes_shouldReturn300(self):
        game = Game()

        for index in range(0, 11):
            game.Roll(10)

        score = game.Score()

        self.assertEqual(score, 300)


if __name__ == '__main__':
    unittest.main()