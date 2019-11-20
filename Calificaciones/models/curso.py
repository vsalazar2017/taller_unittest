# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID
from odoo.exceptions import UserError

class Curso(models.Model):
    _name="res.curso"

    name = fields.Char(
        string="Curso"
    )
    num_cred=fields.Integer(
        string="Creditos"
    )