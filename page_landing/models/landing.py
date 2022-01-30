# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


class LandingPage(models.Model):
    _name = 'landing.page'
    _description = 'Tabla que contiene los clientes de TCM y del POS'
    # _inherit = 'res.users'

    instance = fields.Char("Nombre Instancia/Base Datos de Odoo", required=True)
    # domain = fields.Char("Dominio de Odoo", default='geztion.pro', required=True)
    url_website = fields.Char("Sitio Web Patrón", compute="_compute_website", store=True)
    user_id = fields.Many2one('res.users', ondelete='set null', string='Usuario', default=lambda self: self.env.user)
    password = fields.Text(string='Contraseña', default=False, required=True)
    is_logged = fields.Boolean(string='Autenticado?', default=False)
    access_token = fields.Text(string='API Access Token', default=False)


    @api.multi
    @api.depends('instance')
    def _compute_website(self):
        if self.instance:
            for record in self:
                valuestr = record.instance + ".geztion.pro"
                record.url_website = "https://" + str(valuestr).strip()

    @api.multi
    def redirect_to_page(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/redirect_to_9999',
            'target': 'new',
        }
