import unittest
from bin.localize import Localize
from static_values import *


class MyTestCase(unittest.TestCase):
    def test_english(self):
        localize = Localize('en', True)

        print('ENGLISH TEST:')

        for key, text in ENGLISH_LANG.items():
            print(f'{key} - {text}')

            self.assertEqual(
                localize.get_text(key),
                text
            )  # add assertion here

    def test_russian(self):
        localize = Localize('ru', True)

        print('RUSSIAN TEST:')

        for key, text in RUSSIAN_LANG.items():
            print(f'{key} - {text}')

            self.assertEqual(
                localize.get_text(key),
                text
            )  # add assertion here


if __name__ == '__main__':
    unittest.main()
