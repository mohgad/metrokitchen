# -*- coding: utf-8 -*-

from odoo import models, fields, api


class metrokitchen(models.Model):
    _inherit = 'product.template'
    _description = 'metrokitchen.metrokitchen'

    
    weekday = fields.Selection([
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday')
    ], string='Weekday')

    week_cycle = fields.Char(string='Week Cycle')

  

    # @api.onchange('weekday')
    # def _onchange_weekday(self):
    #     if self.weekday == 'monday':
    #         self.is_published = True
    #     else:
    #         self.is_published = False

