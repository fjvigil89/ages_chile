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

class TCMLandingPage(http.Controller):
    @http.route('/redirect_client_tcm', type='http', auth='user', methods=['GET'], csrf=False)
    def redirect_to_client(self, **kw):
        user_id = http.request.env.context.get('uid')
        print('user_id: ', user_id)

        pool_users = request.env['res.users']
        row_user = pool_users.search([('id', '=', user_id)])

        readPassword = self.read_password(user_id)
        userPassword = readPassword[0]
        # print('Usuario: ', row_user)
        # print('Password: ', userPassword)  # str(list(tuple))

        user_tcm = request.env['tcm.client.landingpage'].search([('user_id.id', '=', user_id)])[0]
        # print('User Id: ', user_tcm.user_id)
        # print('Password UserId: ', user_tcm.password)
        # print('Instancia: ', user_tcm.instance)
        # print('Sitio Web Patrón: ', user_tcm.url_website)

        username = row_user.login
        password = user_tcm.password
        database = user_tcm.instance

        domain_url = user_tcm.url_website
        # domain_url = "https://%s.geztion.pro" % user_tcm.instance
        # domain_url = 'http://192.168.56.101:8069'

        # http://192.168.56.101:8069/login_odoo?db=prueba&login=jramonholy@gmail.com&password=desarrollo&action=mail.action_discuss

        action='mail.action_discuss'
        url = domain_url + '/login_client?db='+database+'&login='+username+'&password='+password+'&action='+action

        return werkzeug.utils.redirect(url)

    @http.route('/redirect_client_pos', type='http', auth='user', methods=['GET'], csrf=False)
    def redirect_to_pos(self, **kw):
        user_id = http.request.env.context.get('uid')
        print('user_id: ', user_id)

        pool_users = request.env['res.users']
        row_user = pool_users.search([('id', '=', user_id)])

        userPassword = self.read_password(user_id)
        # print('Usuario: ', row_user)
        # print('Password: ', userPassword)

        user_tcm = request.env['tcm.client.landingpage'].search([('user_id.id', '=', user_id)])[0]
        # print('User Id: ', user_tcm.user_id)
        # print('Password UserId: ', user_tcm.password)
        # print('Instancia: ', user_tcm.instance)
        # print('Sitio Web Patrón: ', user_tcm.url_website)

        username = row_user.login
        password = user_tcm.password
        database = user_tcm.instance

        # domain_url = "https://%s.geztion.pro" % user_tcm.instance
        # domain_url = 'http://192.168.56.101:8069'
        domain_url = user_tcm.url_website

        # https://9999.geztion.pro/pos/web/#action=pos.ui
        # action = 'point_of_sale.action_pos_config_kanban&model=pos.config&view_type=kanban'
        # action=point_of_sale.action_pos_config&&model=pos.config&view_type=kanban&menu_id=185
        action = 'pos.ui'

        url = domain_url + '/login_pos?db=' + database + '&login=' + username + '&password=' + password + '&action=' + action

        return werkzeug.utils.redirect(url)
