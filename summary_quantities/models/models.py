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
        total_product = 0
        total_delivered = 0
        total_invoice = 0
        for line in self.order_line:
            total_product += line.product_uom_qty
            total_delivered += line.qty_delivered
            total_invoice += line.qty_invoiced

        self.total_product_uom_qty = total_product
        self.total_delivered_qty = total_delivered
        self.total_invoice_qty = total_invoice
