# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID
from odoo.exceptions import UserError

class Nota(models.Model):
    _name ="res.notas"

    @api.multi
    def name_get(self):
        result = []
        for notas in self:
            result.append((notas.id, "%s" % (notas.id)))
        return result

    value = fields.Integer(
        string='Nota final'
    )
    matricula_id = fields.Many2one(
        'res.matricula',
        string="Matricula"
        )
    notas_line = fields.One2many('res.notas.line', 'notas_id', string='notas')


class NotaLine(models.Model):
    _name ="res.notas.line"

    _TRIMESTRE=[
			('1','I'),
			('2','II'),
			('3','III'),
		]
    value = fields.Integer(
        string='Nota'
    )
    term = fields.Selection(_TRIMESTRE,
        string="Trimestre"
    )
    notas_id = fields.Many2one(
        'res.notas',
        string="notas"
        )