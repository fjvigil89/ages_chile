# -*- coding: utf-8 -*-

# from odoo import http
import requests
from requests import Request,Session
import json as json

# url_connect = "https://9999.geztion.pro/web/session/authenticate"
# url = "https://9999.geztion.pro/web/session/get_session_info"
# redirect_url = "https://9999.geztion.pro/web?#action=95&active_id=mailbox_inbox&menu_id=75"

url_connect = "http://192.168.56.101:8069/web/session/authenticate"
url = "http://192.168.56.101:8069/session/get_session_info"
redirect_url = "http://192.168.56.101:8069/web?#action=95&active_id=mailbox_inbox&menu_id=75"

# url = '/web#id={0}&view_type={1}&model={2}'.format(1, 'form', 'res.partner')
headers = {
    'Content-Type': 'application/json'
}

data_connect = {
    "jsonrpc": "2.0",
    "method": "call",
    "id": 1,
    "params": {
        "db": "tcm_module",
        "login": "jramonholy@gmail.com",
        "password": 'desarrollo'
        # "password": "$pbkdf2-sha512$25000$XevdOydkrNXa27tXCgFAKA$XnsxbhBYllJrJXcRWyiVWLv562DQdATILObyWlEU/hSJ5ePXSw/N8GNWAHZ1K4gyobtCXLYWXV.f9Wv3E0ODhg"
    }
}

data = {}

session = Session()

req = Request('POST', url_connect, data=json.dumps(data_connect), headers=headers)

print('Request: ', req)
print("\n")
prepped = req.prepare()
response = session.send(prepped)
print('Response: ', response)
print('Response.headers: ', response.headers)
print('Response.request: ', response.request)
print('Response.cookies: ', response.cookies)
print('Response.text: ', response.text)
print("\n")

r_data = json.loads(response.text)
# print('r_data: ', r_data)

session_id = r_data['result']['session_id']
username = r_data['result']['username']
webbaseurl = r_data['result']['web.base.url']
displayname = r_data['result']['partner_display_name']
db = r_data['result']['db']

print("Print Session del Usuario\n")
print('Session Id:', session_id)
print('Base datos:', db)
print('username:', username)
print('displayname:', displayname)
print('Base Url:', webbaseurl)

# NOW MAKE REQUESTS AND PASS YOUR SESSION ID
cookies = r_data['result']['session_id']
session.cookies['session_id'] = cookies
print('session.cookies:', session.cookies)

# res = requests.get(b_url + "/your/controller/path", cookies={'session_id': str(session_id)})
res = requests.get(redirect_url, cookies={'session_id': str(session_id)})
#
print('res.request:', res.request)
print('res.headers:', res.headers)
print('res.cookies:', res.cookies)
print('res.url:', res.url)
print("\n")
print(res.text)

# http.redirect_with_hash(redirect_url, 303)

# r_data = json.loads(response.text)

# req1 = session.request('POST', url, data=json.dumps(data), headers=headers)
# resp = requests.post(url, data=json.dumps(data), headers=headers)
# print(resp)
# if resp.ok:
#     print('Response url: ', resp.url)
#     print('Response request: ', resp.request)
#     print('Response headers: ', resp.headers)
#     print('Response cookies: ', resp.cookies)
#     print('Response text: ', resp.text)
    #result = resp.json()['result']
    #print('SessionID: ', result.get('session_id'))


#print('Response.headers: ', response.headers)
#print('Response.headers: ', response.request)
#print('Response.cookies: ', response.cookies)


# print('r_data: ', r_data)