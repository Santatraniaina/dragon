
from odoo import fields, models, _

class AttendClassWizard(models.Model):
    _name = 'attend.class.wizard'
    _description = 'Description'

    class_id = fields.Many2one('student.class', string='Class')

    # def assist_class(self):

