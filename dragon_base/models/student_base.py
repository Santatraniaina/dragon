# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentBase(models.Model):
    _name = 'student.base'
    _description = "Student's table"

    name = fields.Char(string="Name")
    lastname = fields.Char(string="Last name")
    birth_date = fields.Date(string="Birth date")
    age = fields.Integer(string="Age")
    matricule = fields.Char(string="Matricule")
    photo = fields.Image(string="Photo")
