# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import requests
from requests import Request,Session
import json as json
import werkzeug as werkzeug
from werkzeug.utils import redirect

from werkzeug import url_encode
from odoo import _, SUPERUSER_ID
from odoo.tools import config

import logging

from odoo.exceptions import except_orm

logger = logging.getLogger(__name__)

class PageLanding(http.Controller):
    def read_password(self, uid):
        # self.ensure_one()
        request.env.cr.execute("SELECT password FROM res_users WHERE id=%s", ( uid,))
        pwd = request.env.cr.fetchall()
        return pwd

    @http.route('/redirect_odoo', type='http', auth='user', methods=['GET'], csrf=False)
    def page_redirect_odoo(self, **kw):
        print("asdasdasd")
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
        # database = user_tcm.instance

        domain_url = "http://localhost:8023"

        action='pos.ui'
        url = domain_url + '/login_odoo?db='+'tcm9999'+'&login='+username+'&password='+password+'&action='+action

        return werkzeug.utils.redirect(url)

    @http.route('/redirect_pos', type='http', auth='user', methods=['GET'], csrf=False)
    def page_redirect_pos(self, **kw):
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

        domain_url = "https://%s.geztion.pro" % user_tcm.instance

        action = 'pos.ui'

        url = domain_url + '/login_pos?db=' + database + '&login=' + username + '&password=' + password + '&action=' + action

        return werkzeug.utils.redirect(url)
