# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StudentClass(models.Model):
    _name = 'student.class'
    _description = "Classes table"

    student_class = fields.Char(copy=False, required=True, readonly=True, default=lambda self: 'New')
    name = fields.Char(string="Name")
    student_number = fields.Integer(string="Student number")
    stage = fields.Char(string="Stage")

    @api.model
    def create(self, vals):
        if vals.get('student_class', 'New') == 'New':
            vals['student_class'] = self.env['ir.sequence'].next_by_code('student.class') or 'New'
        res = super(StudentClass, self).create(vals)
        return res