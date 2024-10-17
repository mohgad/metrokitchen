# -*- coding: utf-8 -*-
from odoo import http, fields
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)

class CustomShopController(WebsiteSale):

    @http.route(['/shop'], type='http', auth="public", website=True)
    def shop(self, **post):
        
        today_date = fields.Date.today()
        today_datetime = datetime.strptime(str(today_date), '%Y-%m-%d')
        weekday = today_datetime.strftime('%A')
        _logger.info('Current weekday: %s', weekday)

        config_param = request.env['ir.config_parameter'].sudo()
        current_cycle = config_param.get_param('week_counter')

        _logger.info('Current cycle: %s', current_cycle)

        published_products = request.env['product.template'].sudo().search([('weekday', '=', weekday.lower()), ('week_cycle', '=', current_cycle)])
        unpublished_products = request.env['product.template'].sudo().search(['|', ('weekday', '!=', weekday.lower()), ('week_cycle', '!=', current_cycle)])
        if published_products:
            published_products.write({'is_published': True})
        unpublished_products.write({'is_published': False})

        
        return super(CustomShopController, self).shop(**post)
        
