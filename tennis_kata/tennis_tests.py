from unittest import TestCase
from tennis_kata.tennis import Tennis


class TestsTennis(TestCase):
    def test_score_should_return_zero_if_no_one_palyer_win_ball(self):
        tennis = Tennis()

        score = tennis.score()

        self.assertEquals(score, "0 - 0")

    def test_core_should_return_15_0_for_one_player_win_ball(self):
        tennis = Tennis()

        tennis.player_one_win()

        score = tennis.score()

        self.assertEquals("15 - 0", score)

    def test_core_should_return_30_15_for_one_player_win_two_balls_and_another_win_one_ball(self):
        tennis = Tennis()

        tennis.player_one_win()
        tennis.player_one_win()

        tennis.player_two_win()

        score = tennis.score()

        self.assertEquals("30 - 15", score)
