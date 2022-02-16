# -*- coding: utf-8 -*-

import requests
from requests import Request, Session
import json as json

# url_connect = "https://9999.geztion.pro/web/session/authenticate"
# url = "https://9999.geztion.pro/web/session/get_session_info"
# redirect_url = "https://9999.geztion.pro/web?#action=95&active_id=mailbox_inbox&menu_id=75"

url_connect = "http://192.168.56.101:8069/web/session/authenticate"
url = "http://192.168.56.101:8069/session/get_session_info"
redirect_url = "http://192.168.56.101:8069/web?#action=95&active_id=mailbox_inbox&menu_id=75"

headers = {'Content-Type': 'application/json'}

data_connect = {
    "jsonrpc": "2.0",
    "method": "call",
    "id": 1,
    "params": {
        "db": "tcm_module",
        "login": "jramonholy@gmail.com",
        "password": "desarrollo"
    }
}

data = {}

session_details = requests.get(url_connect, data=json.dumps(data_connect), headers=headers)
session_id = str(session_details.cookies.get('session_id'))
print('session_id: ', session_id)

session_details.close()

cookies = {
    'username': "jramonholy@gmail.com",
    'password': 'desarrollo',
    'session_id': session_id
    # which we just got in the previous code block
}

resp = requests.get(redirect_url, cookies=cookies)
print('Response.headers: ', resp.headers)
print('Response.headers: ', resp.request)
print('Response.cookies: ', resp.cookies)
print('Response url: ', resp.url)
resp.close()
# print(resp.text)



# import requests
# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry
#
#
# session = requests.Session()
# retry = Retry(connect=3, backoff_factor=0.5)
# adapter = HTTPAdapter(max_retries=retry)
# session.mount('http://', adapter)
# session.mount('https://', adapter)
#
# session.get(url)

