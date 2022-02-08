# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import requests
from requests import Request,Session
import json as json

import xmlrpclib
from openerp.exceptions import except_orm

class PageLanding(http.Controller):
    @http.route('/hello', auth='public')
    def hello(self, **kw):
        return "Hello, world"

    @http.route('/landing', auth='public', website=True)
    def landing(self, **kw):
        return "Hello, page landing"

    @http.route('/db_list', auth='public', website=True)
    def get_db_list(self, **kw):
        dbs = []
        dbs += http.db_list(force=True)
        # dbs += [db for db in http.db_list(force=True)
        #        if db.endswith('_%s' % replace('.', '_'))]
        return http.request.render('pagelanding.get_db_list', {
            'selection_options': dbs
        })

    # http://192.168.56.101:8069/web?debug#action=91&active_id=mailbox_inbox&menu_id=74
    @http.route('/redirect_to_page', type='http', auth='public', website=True)
    def web_login_redirect(self, **kw):
        user_id = http.request.env.context.get('uid')
        user = request.env['res.users'].search([('id', '=', user_id)])[0]
        print('Usuario: ', user)
        #page = request.env['landing.page'].search([('id', '=', user_id)])[0]

        #domain_url = "https://%s.geztion.pro" % page.instance
        #session_authenticate = "/web/session/authenticate"
        #session_info = "/web/session/get_session_info"
        # url_connect = domain_url + session_authenticate

        # base_url = "127.0.0.1:8069"
        # url = "%s/web/session/authenticate" % base_url
        
        # ipdb.set_trace()
        # url_connect = "http://localhost:8889/web/session/authenticate"
        # redirect_url = 'http://localhost:8889/web?action=107&model=mail.message&view_type=list&menu_id=82'

        url_connect = "https://9999.geztion.pro/web/session/authenticate"
        url = "https://9999.geztion.pro/web/session/get_session_info"
        redirect_url = "https://9999.geztion.pro/web?#action=95&active_id=mailbox_inbox&menu_id=75"
        headers = {
            'Content-Type': 'application/json'
        }

        data_connect = {
            "jsonrpc": "2.0",
            "method": "call",
            "id": 1,
            "params": {
                "db": "9999",
                "login": "jramonholy@gmail.com",
                "password": "Maranatha.2021++"
            }
        }

        data = {}

        session = Session()
        req = Request('POST',url_connect,data=json.dumps(data_connect),headers=headers)
        print('Request: ', req)
        print("\n")
        prepped = req.prepare() 
        response = session.send(prepped)
        print('Response: ', response)
        print("\n")

        r_data = json.loads(response.text)
        session_id = r_data['result']['session_id']
        username = r_data['result']['session_id']
        webbaseurl = r_data['result']['web.base.url']
        displayname = r_data['result']['partner_display_name']
        
        db = r_data['result']['db']
        print('Session:', session_id)
        print('Base datos:', db)
        print('username:', username)
        print('displayname:', displayname)
        print('Base Url:', webbaseurl)

        # session_id = json.loads(response.text)['result']['session_id']


        """  session = request.session
        print('Session:', session)
        response = session.post(url=url_connect, data=json.dumps(data_connect), headers=headers)
        print('Response:', response) """

        #uid = ''
        #if response.ok:
        #    result = response.json()['result']
        #    if result.get('session_id'):
        #        session.cookies['session_id'] = result.get('session_id')
        #        uid = result.get('uid')
        #        print('uid:', uid)
        #response = session.post(url=url, data=json.dumps(data), headers=headers)
        #print('Response:', response)
        #return http.redirect_with_hash(redirect_url)

    @http.route('/redirect_to_local', type='http', auth='public')
    def web_redirect_local(self, **kw):

        url = "https://9999.geztion.pro/web/session/authenticate"
        db = "9999"
        user = "jramonholy@gmail.com"
        pwd = "Maranatha.2021++"
        
        # url = 'http://localhost:8069' or ''
        try:
            common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url), allow_none=1)
            uid = common.authenticate(db, user, pwd, {})
            print('Session:', uid)
            if uid == 0:
                raise Exception('Credentials are wrong for remote system access')
            else:
                message = 'Connection Stablished Successfully'
        except Exception as e:
            raise except_orm(_('Remote system access Issue \n '), _(e))
        print('******message*****',message)
        return uid, url, db, common, pwd

        """ b_url = "http://192.168.56.101:8069"
        # or "http://201.100.100.12:8069" (or whatever the ip is)
        url = "{}/web/session/authenticate".format(b_url)
        
        db = "tcm_module"
        user = "jramonholy@gmail.com"
        passwd = "desarrollo"
        
        s = Session()
        
        data = {
            "jsonrpc": "2.0",
            "method": "call",
            "id": 1,
            'params': {
                'context': {},
                'db': db,
                'login': user,
                'password': passwd,
            },
        }
        
        headers = {
            'Content-type': 'application/json'
        }
        
        req = Request('POST',url,data=json.dumps(data),headers=headers)        
        prepped = req.prepare()        
        resp = s.send(prepped)
        print('Response: ', resp)
        print("\n")
        
        session_id = json.loads(resp.text)['result']['session_id']
        
        # NOW MAKE REQUESTS AND PASS YOUR SESSION ID
        
        res = requests.get(b_url + "/redirect_to_local",cookies={'session_id':str(session_id)}) """

        """ 
            self.ensure_one()
            self.env.cr.execute("SELECT password FROM res_users WHERE id=%s", self.id)

            user = models.execute_kw(db, uid, password,
            'res.users', 'search_read',
            [[['id', '=', 2]]],
            {})
        print user """
        
        # print(res.text)
    
    @http.route('/redirect_xmlrpc', auth='public', website=True)
    def web_login_xmlrpc(self, **kw):
        url = "https://9999.geztion.pro/web/session/authenticate"
        db = "9999"
        user = "jramonholy@gmail.com"
        pwd = "Maranatha.2021++"
        
        # url = 'http://localhost:8069' or ''
        try:
            common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url), allow_none=1)
            uid = common.authenticate(db, user, pwd, {})
            print('Session:', uid)
            if uid == 0:
                raise Exception('Credentials are wrong for remote system access')
            else:
                message = 'Connection Stablished Successfully'
        except Exception as e:
            raise except_orm(_('Remote system access Issue \n '), _(e))
        print('******message*****',message)
        return uid, url, db, common, pwd