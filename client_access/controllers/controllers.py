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

import xmlrpc.client


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
        db = kw.get('db_selection')
        username = kw.get('login')
        password = kw.get('password')
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(domain_url))
        try:
            uid = common.authenticate('tc9999', username, password, {})
            pos_config = False
            models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(domain_url))
            session = models.execute_kw('tc9999', uid, password, 'pos.session', 'search_read',
                                        [[['user_id', '=', uid], ['state', '=', 'opened']]])

            # Revisando si el usuario tiene session activa
            if session:
                url = domain_url + '/login_odoo?db=' + 'tc9999' + '&login=' + username + '&password=' + password + '&action=' + action

                return werkzeug.utils.redirect(url)

            # SI NO TIENE SESSION ACTIVA, BUSCAR UN POS para INICIALIZAR
            pos_configs = models.execute_kw('tc9999', uid, password, 'pos.config', 'search_read',
                                            [[]])
            for pos in pos_configs:
                pos_sessions = models.execute_kw('tc9999', uid, password, 'pos.session', 'search_read',
                                                 [[['config_id', '=', pos.get('id')], ['state', '=', 'opened']]])
                if not pos_sessions:
                    pos_config = pos.get('id')
            # IF NOT POS CONFIG ERROR NO ENTRAR!
            # ELSE

            start_session_in_config = models.execute_kw('tc9999', uid, password, 'pos.config', 'open_session_cb',
                                                        [pos_config])

            url = domain_url + '/login_odoo?db=' + 'tc9999' + '&login=' + username + '&password=' + password + '&action=' + action

            return werkzeug.utils.redirect(url)
        except:
            pass

    @http.route('/redirect_odoo', type='http', auth='public', website=True)
    def page_redirect_odoo(self, **kw):
        return http.request.render('page_landing.landing_page_odoo', {
            'url': 'http://localhost:8023/web'
        })
