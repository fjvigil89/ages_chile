# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AccountInvoiceLine(models.Model):
    # TDE FIXME: what is this code ??
    _inherit = "account.invoice"

    check_done = fields.Boolean(string='Sincronizado', default=False)
