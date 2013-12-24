from unittest import TestCase
from bowlingKata.game import Game


class TestGame(TestCase):
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
