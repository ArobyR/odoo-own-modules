# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Invoice(models.Model):
    _name = "invoice.invoice"

    date_invoice = fields.Datetime(default=lambda self: fields.Datetime.now(),
            required=True)
    product_ids = fields.One2many("product.line", "invoice_id")
    partner_id = fields.Many2one("res.partner", string="Partner ID",
            required=True)

    total = fields.Float(compute="_calc_total", string="Total")

    @api.depends("product_ids.subtotal")
    def _calc_total(self):
        for record in self:
            self.total = sum(line.subtotal for line in record.product_ids)
    

class Product(models.Model):
    _name = "product.line"

    invoice_id = fields.Many2one("invoice.invoice", string="Invoice")
    produt_id = fields.Many2one("product.product")
    nombre_product = fields.Char()
    precio = fields.Float(required=True)
    cantidad = fields.Integer(required=True, default=1)
    subtotal = fields.Float(compute="_calc_subtotal")

    @api.depends("precio", "cantidad")
    def _calc_subtotal(self):
        for record in self:
            record.subtotal = record.precio * record.cantidad

    @api.onchange("produt_id")
    def _onchange_product_id(self):
        self.nombre_product = self.produt_id.name
        self.precio = self.produt_id.list_price

