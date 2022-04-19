# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging

log = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    product_limit_list = fields.One2many(
        'product.limit', 'partner_limit', string='Productos limitados')
    category_limit_list = fields.One2many(
        'category.limit', 'partner_id', string='Categoria limitada')

    is_limit_product = fields.Boolean(related='website_id.is_limit_product',
                                      readonly=False)


class ProductProduct(models.Model):
    _name = 'product.limit'
    _description = 'Product limit'

    partner_limit = fields.Many2one('res.partner')
    product = fields.Many2one('product.product', string="Producto")
    limit = fields.Integer("Limite")
    quantity_consumed = fields.Integer("Cantidad consumida")

    def cron_reset_product_qty_consumed_to_zero(self):
        all_quantity_consumed = self.env['product.limit'].search(
            [('quantity_consumed', '>', 0)])

        for qty_obj in all_quantity_consumed:
            qty_obj.quantity_consumed = 0


class CategoryLimit(models.Model):
    _name = 'category.limit'
    _description = 'Category limit'

    partner_id = fields.Many2one('res.partner')
    category_id = fields.Many2one('product.category', string='Category')
    limit = fields.Integer('Limit')
    quantity_consumed = fields.Integer('Consumed Qty')

    def cron_reset_quantity_consumed_to_zero(self):
        all_quantity_consumed = self.env['category.limit'].search(
            []).filtered(lambda x: x.quantity_consumed > 0)

        for qty_obj in all_quantity_consumed:
            qty_obj.quantity_consumed = 0


class Website(models.Model):
    _inherit = 'website'

    is_limit_product = fields.Boolean('Limit by product')


class Settings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_limit_product = fields.Boolean(related='website_id.is_limit_product',
                                      readonly=False)
