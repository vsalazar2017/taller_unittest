# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID
from odoo.exceptions import UserError

class Dictar(models.Model):
    _name = "res.dictar"

    @api.multi
    def name_get(self):
        result = []
        for dictar in self:
            result.append((dictar.id, "%s %s" % (dictar.course and dictar.course.name or '', dictar.teacher and dictar.teacher.name or '')))
        return result

    date_init = fields.Datetime(
        string="Fecha inicio"
    ) 
    date_end = fields.Datetime(
        string="Fecha fin"
    ) 
    teacher = fields.Many2one('res.profesor', string="Profesor")
    course = fields.Many2one('res.curso', string="Curso")