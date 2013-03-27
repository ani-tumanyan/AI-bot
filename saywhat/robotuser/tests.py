from unittest import TestCase
from robotuser.robot import Robot
from robotuser.utility import Utility
from saywhat import settings
import random


class RobotTest(TestCase):
    def test_get_word_length_in_range_success(self):
        word_length = Utility().get_word_length(level=3)
        self.assertGreaterEqual(word_length, settings.WORD_MIN_LENGTH)
        self.assertLessEqual(word_length, settings.WORD_MAX_LENGTH)

    def test_get_word_length_default_success(self):
        word_length = Utility().get_word_length()
        self.assertGreaterEqual(word_length, settings.WORD_MIN_LENGTH)
        self.assertLessEqual(word_length, settings.WORD_MAX_LENGTH)

    def test_get_word_length_negative_or_zero_level_success(self):
        level = random.randrange(-5, 0)
        word_length = Utility().get_word_length(level=level)
        self.assertEqual(word_length, -1)

    def test_get_word_by_length_success(self):
        word = Utility().get_word_by_length(length=5)
        self.assertEqual(len(word), 5)

    def test_get_word_by_length_default_success(self):
        word = Utility().get_word_by_length()
        self.assertEqual(len(word), 5)

    def test_get_word_by_length_fail(self):
        word = Utility().get_word_by_length(length=-5)
        self.assertEqual(len(word), 0)

    def test_generate_letter_list_success(self):
        new_word = Utility().get_word_by_length(length=5)
        letters = Utility().generate_letter_list(existing_letters=list(new_word))

        self.assertEqual(len(letters), settings.MAX_LETTER_COUNT)

    def test_new_game_initial_success(self):
        result = Robot().new_game()

        print "------------------ NEW WORD -------------------------"
        print result
        print "-----------------------------------------------------"

    def test_guess_word_success(self):
        result = Robot().guess_word(word='hello', letters=['a', 'u', 'h', 'p', 'e', 'f', 'l', 'l', 'o'])

        print "------------------ GUESSING THE WORD -------------------------"
        print result
        print "-----------------------------------------------------"
