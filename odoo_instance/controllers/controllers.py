# -*- coding: utf-8 -*-

import odoo
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
from odoo.service import db, security

import logging
# import jinja2

from odoo.exceptions import except_orm

# env = jinja2.Environment(loader=loader, autoescape=True)
# env.filters["json"] = json.dumps

DBNAME_PATTERN = '^[a-zA-Z0-9][a-zA-Z0-9_.-]+$'

logger = logging.getLogger(__name__)

class PartnerForm(http.Controller):
    @http.route('/customer/form', type='http', auth="public", website=True)
    def partner_form(self, **post):
        return request.render("odoo_instance.tmp_customer_form", {})

    @http.route('/customer/form/submit', type='http', auth="public", website=True, csrf=False)
    #next controller with url for submitting data from the form#
    def customer_form_submit(self, **post):
        print('Name: ', post.get('name'))
        print('Email: ', post.get('login'))
        print('Password: ', post.get('password'))
        print('Phone: ', post.get('phone'))
        print('Idioma: ', post.get('lang'))
        print('Pais: ', post.get('country_code'))
        print('Plan: ', post.get('product'))
        print('Metodo de Pago: ', post.get('paymethod'))

        # partner = request.env['res.partner'].create({
        #     'name': post.get('name'),
        #     'email': post.get('email'),
        #     'phone': post.get('phone')
        # })
        vals = {
            'partner': 'ClienteX' # partner,
        }
        print(vals)
        #inherited the model to pass the values to the model from the form#
        return request.render("odoo_instance.tmp_customer_form_success", vals)
        #finally send a request to render the thank you page#

    @http.route('/wizard/platform', type='http', auth="public", website=False, csrf=False)
    def partner_form(self, **kw):
        d = {}
        d['manage'] = True
        d['langs'] = odoo.service.db.exp_list_lang()
        d['countries'] = odoo.service.db.exp_list_countries()
        d['pattern'] = DBNAME_PATTERN
        # databases list
        d['databases'] = []
        # print('Diccionario d:', d)

        return request.render("odoo_instance.wizard_instance", d)
        # return request.env.get_template("wizard_instance.html").render({})
        # Fin de la cita
