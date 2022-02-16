# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import requests
from requests import Request, Session
import json as json
import werkzeug as werkzeug

import logging

from odoo.exceptions import except_orm

logger = logging.getLogger(__name__)


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
        return http.request.render('page_landing.get_db_list', {
            'selection_options': dbs
        })

    def read_password(self, uid):
        # self.ensure_one()
        request.env.cr.execute("SELECT password FROM res_users WHERE id=%s", (uid,))
        pwd = request.env.cr.fetchall()
        return pwd

    @http.route('/web_redirect_odoo', type='http', auth='public', website=True)
    def web_redirect_odoo(self, **kw):
        user_id = http.request.env.context.get('uid')
        print('user_id: ', user_id)

        pool_users = request.env['res.users']
        row_user = pool_users.search([('id', '=', user_id)])

        userPassword = self.read_password(user_id)
        print('Usuario: ', row_user)
        print('Password: ', userPassword)

        user_tcm = request.env['landing.page'].search([('user_id.id', '=', user_id)])[0]
        print('User Id: ', user_tcm.user_id)
        print('Password UserId: ', user_tcm.password)
        print('Instancia: ', user_tcm.instance)
        print('Sitio Web Patrón: ', user_tcm.url_website)

        username = row_user.login
        password = user_tcm.password
        database = user_tcm.instance

        # username = 'jramonholy@gmail.com'
        # password = 'desarrollo'
        # database = 'tcm_module'

        # domain_url = "https://192.168.56.101:8069"
        domain_url = "https://%s.geztion.pro" % user_tcm.instance
        session_authenticate = "/web/session/authenticate"
        session_info = "/web/session/get_session_info"

        url_connect = domain_url + session_authenticate
        url_session = domain_url + session_info
        redirect_url = domain_url + "/web?#action=95&active_id=mailbox_inbox&menu_id=75"

        # url_connect = "https://9999.geztion.pro/web/session/authenticate"
        # url = "https://9999.geztion.pro/web/session/get_session_info"
        # redirect_url = "https://9999.geztion.pro/web?#action=95&active_id=mailbox_inbox&menu_id=75"

        # url_connect = "http://192.168.56.101:8069/web/session/authenticate"
        # url = "http://192.168.56.101:8069/session/get_session_info"
        # redirect_url = "http://192.168.56.101:8069/web?#action=95&active_id=mailbox_inbox&menu_id=75"

        print('url_connect: ', url_connect)
        print('url_session: ', url_session)
        print('redirect_url: ', redirect_url)

        headers = {
            'Content-Type': 'application/json'
        }

        data_connect = {
            "jsonrpc": "2.0",
            "method": "call",
            "id": 1,
            "params": {
                "db": database,
                "login": username,
                "password": password
            }
        }
        data = {}

        session_details = requests.post(url_connect, data=json.dumps(data_connect), headers=headers, verify=False)
        session_id = str(session_details.cookies.get('session_id'))
        print('session_id: ', session_id)
        session_details.close()

        cookies = {
            'username': username,
            'password': password,
            'session_id': session_id
        }

        response = requests.get(redirect_url, cookies=cookies)
        print('Response.headers: ', response.headers)
        print('Response.request: ', response.request)
        print('Response.cookies: ', response.cookies)
        print('Response url: ', response.url)
        # print(resp.text)
        response.close()

        werkzeug.http.dump_cookie('session_id', session_id, max_age=90 * 24 * 60 * 60, httponly=True)
        # print(response.text)

        # werkzeug.http.dump_cookie('session_id', session_id, max_age=90 * 24 * 60 * 60, expires=int(time.time()) + 3 * 3600, httponly=True)
        # return werkzeug.utils.redirect(response.url)

        values = {
            'url': response.url,
            'cookies': response.cookies,
            'session_id': session_id
        }
        return request.render("page_landing.page_redirect_odoo", values)

        # res = requests.get(b_url + "/your/controller/path", cookies={'session_id': str(session_id)})
        # return http.redirect_with_hash('/web_redirect_odoo')

    @http.route('/redirect_odoo', type='http', auth='public', website=True)
    def page_redirect_odoo(self, **kw):
        return http.request.render('page_landing.landing_page_odoo', {
            'url': 'https://9999.geztion.pro/web'
        })
