# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


class LandingPage(models.Model):
    _name = 'landing.page'
    _description = 'Tabla que contiene los clientes de TCM'
    # _inherit = 'res.users'

    instance = fields.Char("Nombre Instancia/Base Datos de Odoo", required=True)
    url_website = fields.Char("Sitio Web Patrón", compute="_compute_website")
    is_logged = fields.Boolean(string='Autenticado?', default=False)
    access_token = fields.Text(string='API Access Token', default=False)
    user_id = fields.Many2one('res.users', ondelete='set null', string='Usuario', default=lambda self: self.env.user)


    @api.multi
    @api.depends('instance')
    def _compute_website(self):        
        self.ensure_one()
        if self.instance:
            self.url_website = "https://" + self.instance + ".geztion.pro"

    @api.multi
    def redirect_to_page(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/redirect_to_9999',
            'target': 'new',
        }

    #@api.model
    #def create(self, vals):
    #    new_record = super().create(vals)
    #    new_record.user_id = self._uid
    #    return new_record
    