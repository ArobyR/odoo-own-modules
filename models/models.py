# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductSale(models.Model):
    _name = 'product.sale'
    _inherit = ['mail.thread']
    _description = 'Product Sale'

    sale_objt = ''

    partner_ids = fields.Many2many("res.partner", string="Partner")
    product_ids = fields.One2many("product.lines", "sale_id")
    total = fields.Float(compute="_calc_total", string="Total")

    def _get_products_formatted(self):
        product_lines = []
        for line in self.product_ids:
            product_lines.append((0, 0, 
                {
                    "product_id": line.product_id.id,
                    "name": line.product_name,
                    "product_uom_qty": line.quantity,
                    "price_unit": line.price,
                    "price_subtotal": line.subtotal
                }
            ))
        return product_lines

    def send_email(self, channel=[], partner_ids=[], body=""):
        # to create channel message_subscribe()
        # to create mail message_post()
        if self.message_subscribe(partner_ids, channel):
            self.message_post(body, subject="Mensaje test")
             
    def create_sale_and_send_email(self):
        sale_names = []
        for line in self.partner_ids:
            sale_objt = self.env["sale.order"].create({
                "partner_id": line.id,
                "order_line": self._get_products_formatted(),
                "date_order": fields.Date.today(),
                }
            )
            sale_names.append(sale_objt["name"])
        
        formatted_sales_names = " ".join(sale_names)
        str_body = f"Listado de nombres: {formatted_sales_names}"

        members = self.env['mail.channel'].browse(6).channel_last_seen_partner_ids
        partner_ids_from_channel = [p.partner_id.id for p in members]
        
        self.send_email([6], partner_ids_from_channel, str_body)
  
    @api.depends("product_ids.subtotal")
    def _calc_total(self):
        """ Calculate the total """ 
        for record in self:
            self.total = sum(line.subtotal for line in record.product_ids)
 

class Product(models.Model):
    _name = 'product.lines'

    sale_id = fields.Many2one("product.sale")
    product_id = fields.Many2one("product.product")
    product_name = fields.Char()
    price = fields.Float()
    quantity = fields.Integer(required=True, default=1)
    subtotal = fields.Float(compute="_calc_subtotal")

    @api.depends("price", "quantity")
    def _calc_subtotal(self):
        """ Calculate the subtotal """ 
        for record in self:
            record.subtotal = record.price * record.quantity

    @api.onchange("product_id")
    def _onchange_product_id(self):
        """ To update the fields """
        self.product_name = self.product_id.name
        self.price = self.product_id.list_price

