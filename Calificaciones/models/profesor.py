# -*- coding: utf-8 -*-

from odoo import models, fields, api, SUPERUSER_ID
from odoo.exceptions import UserError


class Profesor(models.Model):
    _name = 'res.profesor'
    _description = 'Profesor'

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