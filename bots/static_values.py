SIMPLE_BOT: int = 1
RANDOM_BOT: int = 2

BOTS_CLASSES: dict = {
    SIMPLE_BOT: "SimpleBot",
    RANDOM_BOT: "RandomBot",
    # Добавлять сюда новых ботов
}
BOTS_VALIDATION: tuple = (SIMPLE_BOT, RANDOM_BOT)

MAX_ROUNDS: int = 10

CASH_APPROVE: int = 3
CASH_WIN: int = 5
CASH_FAIL: int = 1
