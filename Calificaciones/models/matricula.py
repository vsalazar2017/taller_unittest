# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID
from odoo.exceptions import UserError


class Matricula(models.Model):
    _name="res.matricula"

    @api.multi
    def name_get(self):
        result = []
        for matricula in self:
            result.append((matricula.id, "%s %s" % (matricula.course and matricula.course.name or '', matricula.student and matricula.student.name  or '')))
        return result

    #Columns
    date = fields.Datetime() 
    type_enrollment = fields.Selection([
        ('ordinary','ordinaria'),
		('special','extraordinaria')
        ],
        string="Tipo de matricula"
    )
    course = fields.Many2one('res.curso', string="Curso")
    student = fields.Many2one('res.alumno', string="Alumno")
    ratings = fields.One2many('res.notas', 'matricula_id', string='notas')