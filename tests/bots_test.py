import unittest
from bots.bots_manager import BotsManager
from bots.bots import *


class MyTestCase(unittest.TestCase):
    def test_bots_activate(self):
        bot_manager = BotsManager()
        bot_manager.init_bots(1, 2)

        bot_1: object = bot_manager.bots_data['first_bot']['name']
        bot_2: object = bot_manager.bots_data['second_bot']['name']

        self.assertEqual(bot_1.__str__(), 'Simple Bot')  # add assertion here
        self.assertEqual(bot_2.__str__(), 'Random Bot')  # add assertion here


if __name__ == '__main__':
    unittest.main()
