import json
import requests

class CurrencyConverter:
    BASE_URL = "https://www.amdoren.com/api/currency.php"

    def __init__(self, json_path="currencies.json"):
        self.api_key = "K3NS5f5tx4C57MsE3Msik2dmyqK8JK"
        self.json_path = json_path
        self.currencies = self.load_currencies()

    def load_currencies(self):
        with open(self.json_path, "r") as file:
            return json.load(file)

    def show_all_currencies(self):
        print("\nAvailable Currencies:")
        print("-" * 30)
        for code, name in self.currencies.items():
            print(f"{code} - {name}")
        print("-" * 30)

    def is_valid(self, code):
        return code in self.currencies

    def convert(self, from_currency, to_currency, amount):
        params = {
            "api_key": self.api_key,
            "from": from_currency,
            "to": to_currency,
            "amount": amount
        }

        response = requests.get(self.BASE_URL, params=params)
        data = response.json()

        if data["error"] != 0:
            raise Exception("API Error: " + data["error_message"])

        return data["amount"]
