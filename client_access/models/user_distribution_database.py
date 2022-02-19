from odoo import models, api, fields, _


class UserDistributionDatabase(models.Model):
    _name = "user.distribution.database"

    name = fields.Char(string="RUT")
    url_base = fields.Char(string="Base URL", default="http://155.210.153.12:10022")
    database = fields.Char(string="Database")
