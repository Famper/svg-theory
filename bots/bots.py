class SimpleBot:
    name: str | None = None

    def __init__(self, name: str = 'Simple Bot'):
        self.name: str = name
        self.full_road: list = []

        self.make_step()

    def make_step(self, opponents_past_move=True) -> bool:
        """
        Метод, который делает выбор принять или отказаться от сотрудничества.
        Бот просто копирует предыдущее действие оппонента.
        :param opponents_past_move: Предыдущий шаг оппонента
        """
        self.full_road.append(opponents_past_move)

        return opponents_past_move

    def get_last_step(self) -> bool | str:
        """
        Метод, который возвращает последний выбор
        :return:
        """
        if len(self.full_road) > 0:
            return self.full_road[-1]
        return 'Not found'

    def __str__(self):
        return self.name


class RandomBot:
    name: str | None = None

    def __init__(self, name: str = 'Random Bot'):
        self.name: str = name
        self.full_road: list = []

        self.make_step()

    def make_step(self, *args) -> bool:
        """
        Метод, который делает выбор принять или отказаться от сотрудничества.
        Бот просто делает выбор рандомно.
        """
        import random

        choices: tuple = (False, True)
        bot_choice = random.choice(choices)

        self.full_road.append(bot_choice)

        return bot_choice

    def get_last_step(self) -> bool | str:
        """
        Метод, который возвращает последний выбор
        :return:
        """
        if len(self.full_road) > 0:
            return self.full_road[-1]
        return 'Not found'

    def __str__(self):
        return self.name
