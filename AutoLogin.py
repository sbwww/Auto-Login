import base64
import json

import requests


class AutoLogin(object):
    def __init__(self):
        self.url = "http://a.nuist.edu.cn/index.php/index/login"
        with open('info.json', 'r') as f:
            info = json.load(f)
            self.domain = info['domain']
            self.username = info['username']
            password = info['password']
            self.password = base64.b64encode(
                password.encode()).decode()  # base64加密

    def login(self):
        dv = {  # form data
            'username': self.username,
            'domain': self.domain,
            'password': self.password,
            'enablemacauth': 0
        }
        try:
            res = requests.post(self.url, data=dv)
            res.raise_for_status()
            return r.json()
        except:
            print('error')


if __name__ == '__main__':
    tool = AutoLogin()
    tool.login()
