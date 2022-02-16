# -*- coding: utf-8 -*-
# Copyright 2021 Artem Shurshilov

from odoo import http
from odoo.http import request
import werkzeug
from werkzeug import url_encode
from odoo import _, SUPERUSER_ID
from odoo.tools import config
import odoo.addons.web.controllers.main


class Login(http.Controller):
    @http.route('/login_odoo', type='http', auth='none', methods=['GET'], csrf=False)
    def login_action(self, login, password, action='mail.action_discuss', db=None, force='', mod_file=None, **kw):
        if db and db != request.db:
            raise Exception(_("Could not select database '%s'") % db)
        uid = request.session.authenticate(request.db, login, password)
        url = '/web#%s' % url_encode({'action': action})

        return werkzeug.utils.redirect(url)

    @http.route('/login_pos', type='http', auth='none', methods=['GET'], csrf=False)
    def LoginPOS(self, login, password, action='mail.action_discuss', db=None, force='', mod_file=None, **kw):
        # def _get_login_redirect_url(uid, redirect=None):

        """ Decide if user requires a specific post-login redirect, e.g. for 2FA, or if they are
        fully logged and can proceed to the requested URL
        Override to add direct login to POS. This feature won't work with MFA.
        """
        if not request.session.uid:
            if db and db != request.db:
                raise Exception(_("Could not select database '%s'") % db)
            uid = request.session.authenticate(request.db, login, password)
            # https://9999.geztion.pro/pos/web/#action=pos.ui
            url = '/pos/web/#%s' % url_encode({'action': action})

        return werkzeug.utils.redirect(url)

        # if request.session.uid:  # fully logged
        #     user = request.env['res.users'].browse(uid)
        #     if user.pos_config_id and user.direct_login:
        #         #  Open POS session only if it is already opened by the same user or if it is closed
        #         if not request.env['pos.session'].search_count([
        #                 ('state', '!=', 'closed'),
        #                 ('config_id', '=', 1),  # user.pos_config_id.id),
        #                 ('rescue', '=', False)
        #             ]) > 0:
        #             redirect = user.pos_config_id.open_session_cb()['url']
        #         return redirect or '/web'
        #
        # # partial session (MFA)
        # url = request.env(user=uid)['res.users'].browse(uid)._mfa_url()
        # if not redirect:
        #     return url
        #
        # parsed = werkzeug.urls.url_parse(url)
        # qs = parsed.decode_query()
        # qs['redirect'] = redirect
        # return parsed.replace(query=werkzeug.urls.url_encode(qs)).to_url()

    # odoo.addons.web.controllers.main._get_login_redirect_url = _get_login_redirect_url
