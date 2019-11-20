# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID
from odoo.exceptions import UserError


class Alumno(models.Model):
    _name = 'res.alumno'
    _description = 'alumno'

    #Columns
    name = fields.Char(
        string="Nombre"
    )
    address = fields.Char(
        string="Dirección"
    )
    phone = fields.Char(
        string="Telefono"
    )
    email = fields.Char(
        string="Correo"
    )
