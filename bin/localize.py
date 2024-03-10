import json


class Localize:
    def __init__(self, language: str, is_test: bool = False):
        """
        Localize - Класс для работы с локализацией
        :param language: **EN** or **RU**
        """
        self.language: str = language
        self.is_test: bool = is_test
        self.localize_text: dict = self.set_list()

    def set_list(self) -> dict | Exception:
        """
        Метод, который возвращает словарь из нужных предложений с локализацией
        :return:
        """
        try:
            if self.is_test:
                path = f'../localize/{str(self.language).lower()}.json'
            else:
                path = f'localize/{str(self.language).lower()}.json'

            with open(path, 'r') as localize_file:
                json_text = localize_file.read()

                return json.loads(json_text)
        except Exception as e:
            raise RuntimeError(e)

    def get_text(self, key: str) -> str | Exception:
        """
        Метод, который возвращает текст по запросу ключа. Возвращает на нужном языке.
        :param key: Ключ текста
        :return: Текст
        """
        if isinstance(self.localize_text, dict):
            text: str | bool = self.localize_text.get(key, False)

            if text:
                return text
        raise RuntimeError("Text not founded")

    def set_new_language(self, language):
        """
        Метод, который задает новую локализацию
        :param language: Новый язык
        :return:
        """
        self.language = language

        self.localize_text = self.set_list()
