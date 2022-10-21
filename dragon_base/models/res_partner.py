from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    nif = fields.Char(string='NIF')
    stat = fields.Char(string='STAT')
    rcs = fields.Char(string='RCS')