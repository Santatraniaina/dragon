from odoo import fields, models

class Professor(models.Model):
    _inherit = 'res.partner'

    tif = fields.Char(string='TIF')
    stat = fields.Char(string='STAT')
    rcs = fields.Char(string='RCS')