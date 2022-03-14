import json
import requests


class Calculator:

    @staticmethod
    def add(a: int, b: int) -> int:
        return a+b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        return a-b

    @staticmethod
    def divide(a: int, b: int) -> int:
        if b == 0:
            raise ValueError('Denominator cannot be 0')
        return a//b

    @staticmethod
    def mulitply(a: int, b: int) -> int:
        return a*b

    @staticmethod
    def calculator_api(a: int, b: int) -> int:
        try:
            response = requests.post('http://api.mathjs.org/v4/',
                                     headers={"Content-Type": "application/json"}, data=json.dumps({"expr": [f'{a}+{b}']}))
            response = response.json()
            if response['error']:
                raise Exception()
            return int(response['result'][0])
        except Exception:
            return 'Bad Request'

