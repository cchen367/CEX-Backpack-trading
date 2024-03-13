import base64
import json
import time
import requests
from cryptography.hazmat.primitives.asymmetric import ed25519
import logging

logging.basicConfig(level=logging.DEBUG)


class BpxClient:
    url = 'https://api.backpack.exchange/'
    private_key = ed25519.Ed25519PrivateKey

    def __init__(self):
        self.debug = False
        self.proxies = {
            'http': '',
            'https': ''
        }
        self.api_key = ''
        self.api_secret = ''
        self.window = 5000
        # self.private_key = ed25519.Ed25519PrivateKey

    def init(self, api_key, api_secret):
        self.api_key = "bCSB5g7gofbPAci1a3+aFgxLMhnzAyEMCefbQxD02D8="
        self.api_secret = "pUbMZYqQ8RLwKcXvxyz+qSSV3CP2q4xS6rrX9h4L7p4="
        self.private_key = ed25519.Ed25519PrivateKey.from_private_bytes(
            base64.b64decode(api_secret)
        )
    def deposits(self):
        return requests.get(url=f'{self.url}wapi/v1/capital/deposits', proxies=self.proxies,
                            headers=self.sign('depositQueryAll', {})).json()

    def depositAddress(self, chain: str):
        params = {'blockchain': chain}
        return requests.get(url=f'{self.url}wapi/v1/capital/deposit/address', proxies=self.proxies, params=params,
                            headers=self.sign('depositAddressQuery', params)).json()

    def getticker(self, symbol: str):
        params = {'symbol': symbol}
        return requests.get(url=f'{self.url}api/v1/ticker', proxies=self.proxies, params=params).json()

    def withdrawals(self, limit: int, offset: int):
        params = {'limit': limit, 'offset': offset}
        return requests.get(url=f'{self.url}wapi/v1/capital/withdrawals', proxies=self.proxies, params=params,
                            headers=self.sign('withdrawalQueryAll', params)).json()

    # history

    def orderHistoryQuery(self, symbol: str, limit: int, offset: int):
        params = {'symbol': symbol, 'limit': limit, 'offset': offset}
        return requests.get(url=f'{self.url}wapi/v1/history/orders', proxies=self.proxies, params=params,
                            headers=self.sign('orderHistoryQueryAll', params)).json()

    def orderHistoryQueryAll(self):
        params = {}
        response = requests.get(url=f'{self.url}wapi/v1/history/orders', proxies=self.proxies, params=params,
                            headers=self.sign('orderHistoryQueryAll', params)).json()
        # logging.debug(f"Request Headers: {response.request.headers}")
        # logging.debug(f"Request Body: {response.request.body}")
        # logging.debug(f"Response Status Code: {response.status_code}")
        # logging.debug(f"Response Headers: {response.headers}")
        # logging.debug(f"Response Content: {response.text}")
        # print(response.status_code)
        print(response)
        return response

    def fillHistoryQuery(self, symbol: str, limit: int, offset: int):
        params = {'limit': limit, 'offset': offset}
        if len(symbol) > 0:
            params['symbol'] = symbol
        return requests.get(url=f'{self.url}wapi/v1/history/fills', proxies=self.proxies, params=params,
                            headers=self.sign('fillHistoryQueryAll', params)).json()

    # order

    def ExeOrder(self, symbol, side, orderType, timeInForce, quantity, price):
        params = {
            'symbol': symbol,
            'side': side,
            'orderType': orderType,
            'timeInForce': timeInForce,
            'quantity': quantity,
            'price': price
        }
        return requests.post(url=f'{self.url}api/v1/order', proxies=self.proxies, data=json.dumps(params),
                             headers=self.sign('orderExecute', params)).json()
    # capital
    def balances(self):
        response = requests.get(
            url=f'{self.url}api/v1/capital',
            proxies=self.proxies,
            headers=self.sign('balanceQuery', {})).json()
        # print(response.status_code)
        print(response)
        return response

    def sign(self, instruction: str, params: dict):
        sign_str = f"instruction={instruction}" if instruction else ""
        sorted_params = "&".join(
            f"{key}={value}" for key, value in sorted(params.items())
        )
        if sorted_params:
            sign_str += "&" + sorted_params
        ts = int(time.time() * 1e3)

        sign_str += f"&timestamp={ts}&window={self.window}"
        signature_bytes = self.private_key.sign(sign_str.encode())
        # signature_bytes = self.private_key.sign(self.private_key, data=sign_str.encode("utf-8"))
        encoded_signature = base64.b64encode(signature_bytes).decode()

        if self.debug:
            print(f'Waiting Sign Str: {sign_str}')
            print(f"Signature: {encoded_signature}")

        headers = {
            "X-API-Key": self.api_key,
            "X-Signature": encoded_signature,
            "X-Timestamp": str(ts),
            "X-Window": str(self.window),
            "Content-Type": "application/json; charset=utf-8",
        }
        return headers



obj = BpxClient()
obj.init(api_key="bCSB5g7gofbPAci1a3+aFgxLMhnzAyEMCefbQxD02D8=", api_secret="pUbMZYqQ8RLwKcXvxyz+qSSV3CP2q4xS6rrX9h4L7p4=")
obj.balances()
obj.orderHistoryQueryAll()
obj.getticker('SOL')