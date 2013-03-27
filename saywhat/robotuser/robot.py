from robotuser.utility import Utility


class Robot(object):
    def new_game(self, *args, **kwargs):
        '''Creates a new word to be guessted by the user.

        Keyword arguments:
        level -- the user's game level

        Returns: dictionary of the created word and list of letters

        '''

        level = kwargs.get('level', 1)

        word_length = Utility().get_word_length(level=level)
        new_word = Utility().get_word_by_length(length=word_length)
        letters = Utility().generate_letter_list(existing_letters=list(new_word))

        return {'word': new_word, 'letters': letters}

    def guess_word(self, *args, **kwargs):
        '''Makes a couple of word guessing attempts.

        Keyword arguments:
        level -- the user's game level
        word -- the correct word
        letters -- the list of letters

        Returns: a list of attempted words during the process of guessing

        '''

        level = kwargs.get('level', 1)
        correct_word = kwargs.get('word', '')
        letters = kwargs.get('letters', [])

        attempts_number = Utility().get_attempts_number(level=level)
        attempts = []

        if attempts_number == 0:
            attempts = [correct_word]

        else:
            word_result = None
            while attempts_number > 0:
                guess_word = Utility().generate_word(letters=letters, word_length=len(correct_word), word_result=word_result)
                attempts.append(guess_word)

                result = Utility().compare_words(guessed_word=guess_word, correct_word=correct_word)
                word_result = result['word_result']

                if result['is_correct']:
                    return attempts

                attempts_number -= 1

            attempts.append(correct_word)

        return attempts
