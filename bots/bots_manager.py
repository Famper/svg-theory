from bots.bots import *
from .static_values import *


class BotsManager:
    list_bots: str | None
    bots_data: dict[str, dict[str, int | None] | dict[str, int | None]]

    def __init__(self):
        """
        Менеджер ботов
        """
        self.list_bots = None
        self.bots_data = {
            'first_bot': {
                'name': None,
                'cash': 0,
                'last_step': None
            },
            'second_bot': {
                'name': None,
                'cash': 0,
                'last_step': None
            },
        }

        self.get_list_of_bots()

    def get_list_of_bots(self) -> None:
        """
        Метод, который генерирует список всех существующих ботов.
        """
        text: str = ''

        for index, bot in BOTS_CLASSES.items():
            text += f'\n\t{index} - {bot}'

        self.list_bots = text

    def init_bots(self, first_bot: int | None = None, second_bot: int | None = None) -> None:
        """
        Инициализация ботов, как объекты класса
        :param first_bot: ID первого бота
        :param second_bot: ID второго бота
        """
        if first_bot:
            self.bots_data['first_bot']['name'] = globals()[BOTS_CLASSES[first_bot]]()
            self.bots_data['first_bot']['last_step'] = self.bots_data['first_bot']['name'].get_last_step()

        if second_bot:
            self.bots_data['second_bot']['name'] = globals()[BOTS_CLASSES[second_bot]]()
            self.bots_data['second_bot']['last_step'] = self.bots_data['second_bot']['name'].get_last_step()

    def rounds(self) -> tuple:
        for _round in range(1, MAX_ROUNDS):
            first_bot_step = self.bots_data['first_bot']['name'].make_step(
                self.bots_data['second_bot']['last_step']
            )
            second_bot_step = self.bots_data['second_bot']['name'].make_step(
                self.bots_data['first_bot']['last_step']
            )

            self.bots_data['first_bot']['last_step'] = self.bots_data['first_bot']['name'].get_last_step()
            self.bots_data['second_bot']['last_step'] = self.bots_data['second_bot']['name'].get_last_step()

            if first_bot_step and second_bot_step:
                self.bots_data['first_bot']['cash'] += CASH_APPROVE
                self.bots_data['second_bot']['cash'] += CASH_APPROVE
            elif first_bot_step or second_bot_step:
                if first_bot_step:
                    self.bots_data['first_bot']['cash'] += CASH_WIN
                else:
                    self.bots_data['second_bot']['cash'] += CASH_WIN
            else:
                self.bots_data['first_bot']['cash'] += CASH_FAIL
                self.bots_data['second_bot']['cash'] += CASH_FAIL

        return (
            self.bots_data['first_bot']['name'].__str__(),
            self.bots_data['first_bot']['cash'],
            self.bots_data['first_bot']['name'].full_road,
            self.bots_data['second_bot']['name'].__str__(),
            self.bots_data['second_bot']['cash'],
            self.bots_data['second_bot']['name'].full_road
        )

    def reset_data(self):
        self.bots_data = {
            'first_bot': {
                'name': None,
                'cash': 0,
                'last_step': None
            },
            'second_bot': {
                'name': None,
                'cash': 0,
                'last_step': None
            },
        }
