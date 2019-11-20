# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Customer(models.Model):
    _name = 'customer'
    
    @api.depends('number_of_sales')
    def _compute_type_customer(self):
        '''
        
        '''
        if self.number_of_sales < 10:
            self.type = "standard"
     
        elif self.number_of_sales >= 10 and self.number_of_sales < 50:
            self.type = "premiun"
     
        else:
            self.type = "vip"
            
    #Columns 
    name = fields.Char(
        string="Cliente",
        required=True
        )
    address = fields.Text(
        string="Dirección"
    )
    email = fields.Char(
        string="Correo"
    )
    number_of_sales = fields.Integer(
        string="Número de ventas"
    )
    type = fields.Selection(
        [
            ('vip', 'VIP'),
            ('premiun', 'Premiun'),
            ('standard', 'Standard')],
        string="Tipo de cliente",
        compute="_compute_type_customer"
    )