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
    def login_pos(self, login, password, action='pos.ui', db=None, force='', mod_file=None, **kw):
        """ Decide if user requires a specific post-login redirect, e.g. for 2FA, or if they are
        fully logged and can proceed to the requested URL
        Override to add direct login to POS. This feature won't work with MFA.
        """
        url = '/web'
        if not request.session.uid:
            if db and db != request.db:
                raise Exception(_("Could not select database '%s'") % db)
            uid = request.session.authenticate(request.db, login, password)
            # https://9999.geztion.pro/pos/web/#action=pos.ui

        url = '/pos/web/#%s' % url_encode({'action': action})
        return werkzeug.utils.redirect(url)
