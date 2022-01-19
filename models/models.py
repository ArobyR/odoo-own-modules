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

    # First get the information of product_ids
    # Call the function and return the list formated with the data
    def _get_products_formated(self):
        product_lines = []
        for line in self.product_ids:
            product_lines.append((0, 0, 
                    {
                        "product_id": line.product_id.id,
                        "account_id": 159,
                        "name": line.nombre_product,
                        "quantity": line.cantidad,
                        "price_unit": line.precio,
                        "price_subtotal": line.subtotal
                    }))
        return product_lines

    def inherited_action(self):
        self.env["account.move"].create({
                "partner_id": self.partner_id.id,
                "invoice_date": self.date_invoice,
                "invoice_line_ids": self._get_products_formated(),
                "move_type": "out_invoice",
            })

    @api.depends("product_ids.subtotal")
    def _calc_total(self):
        for record in self:
            self.total = sum(line.subtotal for line in record.product_ids)
    

class Product(models.Model):
    _name = "product.line"

    invoice_id = fields.Many2one("invoice.invoice", string="Invoice")
    product_id = fields.Many2one("product.product")
    nombre_product = fields.Char()
    precio = fields.Float(required=True)
    cantidad = fields.Integer(required=True, default=1)
    subtotal = fields.Float(compute="_calc_subtotal")

    @api.depends("precio", "cantidad")
    def _calc_subtotal(self):
        for record in self:
            record.subtotal = record.precio * record.cantidad

    @api.onchange("product_id")
    def _onchange_product_id(self):
        self.nombre_product = self.product_id.name
        self.precio = self.product_id.list_price

