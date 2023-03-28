import requests
import json
from config import keys

class APIException(Exception):
    pass

class СurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать колличество {amount}.')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/6c649b749f08b2ae662a2dfe/pair/{quote_ticker}/{base_ticker}')
        total_base = json.loads(r.content).values()

        return total_base