# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_product_uom_qty = fields.Float(
        compute="_compute_total_quantities",
        string="Pedidas",
        store=True,
    )
    total_delivered_qty = fields.Float(
        compute="_compute_total_quantities",
        string="Despachadas",
        store=True,
    )
    total_invoice_qty = fields.Float(
        compute="_compute_total_quantities",
        string="Facturadas",
        store=True,
    )

    @api.depends('order_line.product_uom_qty', 'order_line.qty_delivered',
                 'order_line.qty_invoiced')
    def _compute_total_quantities(self):
        for record in self:
            record.total_product_uom_qty = sum(
                record.order_line.mapped('product_uom_qty'))
            record.total_delivered_qty = sum(
                record.order_line.mapped('qty_delivered'))
            record.total_invoice_qty = sum(
                record.order_line.mapped('qty_invoiced'))
