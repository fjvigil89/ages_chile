# -*- coding: utf-8 -*-
# from odoo import http
import json
import ssl

import requests
import werkzeug

import odoo
import xmlrpc.client

from odoo import http
from odoo.http import content_disposition, dispatch_rpc, request


class Controllers(http.Controller):

    @http.route('/access-client', auth='public', website=True)
    def access_client_controller(self, **kw):
        dbs = []
        dbs += http.db_list(force=True)
        # dbs += [db for db in http.db_list(force=True)
        #        if db.endswith('_%s' % replace('.', '_'))]
        return http.request.render('client_access.access_client_page_template', {
            'selection_options': dbs
        })

    @http.route('/web/login/access', type='http', auth="none", sitemap=False)
    def web_login(self, redirect=None, **kw):
        domain_url = "http://localhost:8023"
        action = 'pos.ui'
        username = 'admin'
        password = 'admin'
        url = domain_url + '/login_odoo?db=' + '9999' + '&login=' + username + '&password=' + password + '&action=' + action
        return werkzeug.utils.redirect(url)

    @http.route('/redirect_odoo', type='http', auth='public', website=True)
    def page_redirect_odoo(self, **kw):
        return http.request.render('page_landing.landing_page_odoo', {
            'url': 'http://localhost:8023/web'
        })
