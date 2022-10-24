# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
class StudentBase(models.Model):
    _name = 'student.base'
    _description = "Student's table"

    student_number = fields.Char(copy=False, required=True, readonly=True, default=lambda self: 'New')
    name = fields.Char(string="Name")
    lastname = fields.Char(string="Last name")
    birth_date = fields.Date(string="Birth date")
    age = fields.Integer(string="Age")
    matricule = fields.Char(string="Matricule")
    photo = fields.Image(string="Photo")

    @api.model
    def create(self, vals):
       if vals.get('student_number','New') == 'New':
           vals['student_number'] = self.env['ir.sequence'].next_by_code('student.base') or 'New'
       res = super(StudentBase, self).create(vals)
       return res

    def create_wizard(self):
        return {
            'name': _('Attend Class Wizard'),
            'type': 'ir.actions.act_window',
            'res_model': 'attend.class.wizard',
            'view_mode': 'form',
            'target': 'new'
        }