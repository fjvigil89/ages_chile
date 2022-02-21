# -*- coding: utf-8 -*-
# from odoo import http
import json
import ssl

import requests
import werkzeug

import odoo
import xmlrpc.client
import logging

from odoo import http, _
from odoo.http import content_disposition, dispatch_rpc, request

_logger = logging.getLogger(__name__)
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

    @http.route('/web/login/access', type='http', auth="none", sitemap=False, website=True)
    def web_login(self, redirect=None, **kw):
        values = request.params.copy()
        action = 'pos.ui'
        db = ''
        if not request.uid:
            request.uid = odoo.SUPERUSER_ID
        domain_url = ''
        rut = kw.get('rut')
        distribution = request.env['user.distribution.database'].sudo().search([["name", "=", rut]])
        if distribution:
            db = distribution.database.strip()
            domain_url = distribution.url_base.strip()
        else:
            values['error'] = _("No existe configuracion para el RUT %s" % rut)
            return request.render('client_access.access_client_page_template', values)

        if not db:
            values['error'] = _("El RUT %s no se relaciona con ninguna base de datos existente" % rut)
            return request.render('client_access.access_client_page_template', values)

        username = kw.get('login')
        password = kw.get('password')
        old_uid = request.uid

        try:
            common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(domain_url))

            uid = common.authenticate(db, username, password, {})
            if not uid:
                values['error'] = _("Usuario o contraseña incorrecta")
                return request.render('client_access.access_client_page_template', values)

            pos_config = False
            models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(domain_url))
            session = models.execute_kw(db, uid, password, 'pos.session', 'search_read',
                                        [[['user_id', '=', uid], ['state', '=', 'opened']]])

            # Revisando si el usuario tiene session activa
            if session:
                url = domain_url + '/login_odoo?db=' + db + '&login=' + username + '&password=' + password + '&action=' + action

                return werkzeug.utils.redirect(url)

            # SI NO TIENE SESSION ACTIVA, BUSCAR UN POS para INICIALIZAR
            pos_configs = models.execute_kw(db, uid, password, 'pos.config', 'search_read',
                                            [[]])
            if not pos_configs:
                values['error'] = _("No existen cajas para iniciar la sesión")
                return request.render('client_access.access_client_page_template', values)

            for pos in pos_configs:
                pos_sessions = models.execute_kw(db, uid, password, 'pos.session', 'search_read',
                                                 [[['config_id', '=', pos.get('id')], ['state', '=', 'opened']]])
                if not pos_sessions:
                    pos_config = pos.get('id')
            if not pos_config:
                values['error'] = _("No existen cajas disponibles para iniciar sesión.")
                return request.render('client_access.access_client_page_template', values)
            # IF NOT POS CONFIG ERROR NO ENTRAR!
            # ELSE

            start_session_in_config = models.execute_kw(db, uid, password, 'pos.config', 'open_session_cb',
                                                        [pos_config])

            url = domain_url + '/login_odoo?db=' + db + '&login=' + username + '&password=' + password + '&action=' + action

            return werkzeug.utils.redirect(url)
        except:
            pass

        return request.render('client_access.access_client_page_template', values)

    @http.route('/redirect_odoo', type='http', auth='public', website=True)
    def page_redirect_odoo(self, **kw):
        return http.request.render('page_landing.landing_page_odoo', {
            'url': 'http://localhost:8023/web'
        })
