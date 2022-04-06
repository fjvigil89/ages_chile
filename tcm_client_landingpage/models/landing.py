# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


class LandingPage(models.Model):
    _name = 'tcm.client.landingpage'
    _description = 'Tabla que contiene los clientes de TCM y del POS'
    # _inherit = 'res.users'

    # instance = fields.Char("Nombre de Instancia Cliente", default='XXXX', required=True)
    ip_server = fields.Char("IP o Dominio del Servidor", default='127.0.0.1', required=True)
    protocol = fields.Selection([('http', 'Protocolo HTTP'),
                                 ('https', 'Protocolo HTTPS')], string='Protocolo de Acceso',
                                        default='http')
    url_website = fields.Char("URL de Acceso", compute="_compute_website", store=True)
    user_id = fields.Many2one('res.users', ondelete='set null', string='Usuario', default=lambda self: self.env.user)
    password = fields.Text(string='Contraseña', default=False, required=True)
    is_logged = fields.Boolean(string='Autenticado?', default=False)
    access_token = fields.Text(string='API Access Token', default=False)


    @api.multi
    @api.depends('ip_server')
    def _compute_website(self):
        if self.ip_server:
            for record in self:
                url = ""
                if record.ip_server:
                    url = str(record.ip_server).strip()
                    print('URL: ', url)
                record.url_website = record.protocol+"://%s" % str(url).strip()
                print('URL: ', record.url_website)

    @api.multi
    def redirect_to_page(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/redirect_to_client',
            'target': 'new',
        }
