from odoo import models, api, fields, _


class UserDistributionDatabase(models.Model):
    _name = "user.distribution.database"

    name = fields.Char(string="RUT")
    database = fields.Char(string="Database")
