from bin.static_values import *
from bin.localize import Localize
from bots.bots_manager import BotsManager
from bots.static_values import BOTS_VALIDATION


class ConsoleManager:
    def __init__(self):
        self.user_input: str | None = None
        self.language: str = LANGUAGES[1]
        self.state: int = START
        self._localize: Localize = Localize(self.language)
        self.bot_manager: BotsManager = BotsManager()

    def input_validation(self, validation: tuple | list) -> bool:
        """
        Валидация введенных данных
        :param validation:
        :return:
        """
        return str(self.user_input).isdigit() and int(self.user_input) in validation

    def start_or_change_language(self, is_change=False) -> None:
        """
        Метод для старта или изменения языка
        :param is_change: Нужно ли менять язык
        """
        if is_change:
            self.user_input = input(self._localize.get_text('select_language'))
        else:
            self.user_input = input(self._localize.get_text('welcome'))

        while True:
            if self.input_validation(LANGUAGES_VALIDATIONS):
                self._localize.set_new_language(LANGUAGES[int(self.user_input)])
                self.state = MAIN_MENU

                break
            else:
                self.user_input = input(self._localize.get_text('error_validation'))

        self.run()

    def main_menu(self):
        self.user_input = input(self._localize.get_text('main_menu'))

        while True:
            if self.input_validation(MAIN_MENU_VALIDATIONS):
                self.user_input = int(self.user_input)

                if self.user_input == START_SIMULATION:
                    print(self._localize.get_text('list_of_bots').format(str(self.bot_manager.list_bots)))

                    while True:
                        self.user_input = input(self._localize.get_text('select_first_bot'))

                        if self.input_validation(BOTS_VALIDATION):
                            self.bot_manager.init_bots(
                                first_bot=int(self.user_input)
                            )
                            break
                        else:
                            self.user_input = input(self._localize.get_text('error_validation'))

                    while True:
                        self.user_input = input(self._localize.get_text('select_second_bot'))

                        if self.input_validation(BOTS_VALIDATION):
                            self.bot_manager.init_bots(
                                second_bot=int(self.user_input)
                            )
                            break
                        else:
                            self.user_input = input(self._localize.get_text('error_validation'))

                    self.state = SHOW_RESULT
                    self.run()
                elif self.user_input == SELECT_LANGUAGE:
                    self.start_or_change_language(True)
                else:
                    print(self._localize.get_text('goodbye'))
                    exit(0)
            else:
                self.user_input = input(self._localize.get_text('error_validation'))

    def show_result(self):
        results: tuple = self.bot_manager.rounds()

        print(
            self._localize.get_text('result').format(
                str(results[0]),
                str(results[1]),
                ', '.join(str(int(element)) for element in results[2]),
                str(results[3]),
                str(results[4]),
                ', '.join(str(int(element)) for element in results[5]),
            )
        )
        self.bot_manager.reset_data()
        self.state = MAIN_MENU
        self.run()

    def run(self):
        print('~' * 10)
        self.user_input = None

        while True:
            if self.state == START:
                self.start_or_change_language()
            elif self.state == MAIN_MENU:
                self.main_menu()
            elif self.state == SHOW_RESULT:
                self.show_result()
            else:
                print('Error')
                exit(0)
