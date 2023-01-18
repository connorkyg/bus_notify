import os
import json
import requests

from config import secrets


class auth:
    def __init__(self):
        self.method = None
        self.api = None
        self.baseurl = 'https://kauth.kakao.com'

    def get_token(self):
        path = './kakao_code.json'
        if os.path.isfile(path):
            with open(path, 'r') as f:
                token = f.read()
            return token
        elif not os.path.isfile(path):
            self.method = 'GET'
            api = '/oauth/token'
            rest_api_key = secrets.KEYS['rest_api']
            redirect_uri = secrets.URI['redirect_uri']
            authorize_code = secrets.code
            data = {
                'grant_type': 'authorization_code',
                'client_id': rest_api_key,
                'redirect_uri': redirect_uri,
                'code': authorize_code,
            }
            response = requests.post(method=self.method, url=self.baseurl + api, data=data)
            token = response.json()
            path = './kakao_code.json'
            with open(path, 'w+') as f:
                json.dump(token, f)
            return token

    def get_authcode(self):
        self.method = 'GET'
        api = '/oauth/authorize'
        params = {
            'client_id': f"{secrets.KEYS['rest_api']}",
            'redirect_uri': f"{secrets.URI['redirect_uri']}",
            'response_type': 'code'
        }
        response = requests.request(method=self.method, url=self.baseurl + api, params=params)
        print(response.url)


if __name__ == '__main__':
