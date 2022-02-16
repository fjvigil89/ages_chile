# -*- coding: utf-8 -*-

# import xmlrpc.client as xmlrpc
from xmlrpc import client

# from odoo.exceptions import except_orm

#url = "https://9999.geztion.pro"
#db = "9999"
url = "127.0.0.1:8069"
db = "tcm_module"
user = "jramonholy@gmail.com"
# pwd = "$pbkdf2-sha512$25000$1nrv/X8PYcx5j7EWopQyxg$JFA8M1bL7CAiSeq4r5mu8LvrjVKKppPsJAC5bNKVqFXllCZ9SNDu9/ogVeadvBe.LXo5625w0cxEBRTh2RK4jQ"
pwd = "Maranatha.2021++"

# url = 'http://localhost:8069' or ''
try:
    common = client.ServerProxy('{}/xmlrpc/2/common'.format(url), allow_none=1)
    print(common.version())
    # common = xmlrpc.ServerProxy('{}/web/session/authenticate'.format(url), allow_none=1)
    user_id = common.authenticate(db, user, pwd, {})
    print('Session:', user_id)
    if user_id:
        message = 'Connection Stablished Successfully'
        print("Success: User id is", user_id)
    else:
        print("Failed: wrong credentials")
    # if uid == 0:
    #     raise Exception('Credentials are wrong for remote system access')
    # else:
    #     message = 'Connection Stablished Successfully'
except Exception as e:
        message = 'Remote system access Issue %s\n ' % e
        # raise except_orm. (_('Remote system access Issue \n '), _(e))
print('******message*****', message)

