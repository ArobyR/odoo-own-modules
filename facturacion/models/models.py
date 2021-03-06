# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Invoice(models.Model):
    _name = "invoice.invoice"

    date_invoice = fields.Datetime(default=lambda x: fields.Datetime.now(),
                                   required=True)
    product_ids = fields.One2many("product.line", "invoice_id")
    partner_id = fields.Many2one("res.partner", string="Partner ID",
                                 required=True)

    total = fields.Float(compute="_calc_total", string="Total")

    link = ""
    invoice_generated = fields.Many2one("account.move")

    def _get_products_formatted(self):
        """ Return a list products formatted
            Create a void list (product_lines)
            And then get the information of product_ids
            later add the values to the product_lines with
            format for return it.
        """
        product_lines = []
        for line in self.product_ids:
            product_lines.append((0, 0,
                                  {
                                      "product_id": line.product_id.id,
                                      "account_id": 159,
                                      "name": line.product_name,
                                      "quantity": line.quantity,
                                      "price_unit": line.price,
                                      "price_subtotal": line.subtotal
                                  }
                                  ))
        return product_lines

    def inherited_action(self):
        """ An action using account.move model
            the purpose is interact with other module
            for example in this case we're creating 
            a invoice in other module with the method create()
            and finally relates what contains link with invoice 
            generated in order to do some things
        """
        link = self.env["account.move"].create({
            "partner_id": self.partner_id.id,
            "invoice_date": self.date_invoice,
            "invoice_line_ids": self._get_products_formatted(),
            "move_type": "out_invoice",
        })
        self.invoice_generated = link.id

    def action_validate(self):
        """ confirm the invoice """
        self.invoice_generated.action_post()

    @api.depends("product_ids.subtotal")
    def _calc_total(self):
        """ Calculate the total """
        for record in self:
            self.total = sum(line.subtotal for line in record.product_ids)


class Product(models.Model):
    _name = "product.line"

    # Bidirectional relation
    invoice_id = fields.Many2one("invoice.invoice", string="Invoice")
    product_id = fields.Many2one("product.product")
    product_name = fields.Char()
    price = fields.Float(required=True)
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


class Client(models.Model):
    _inherit = "res.partner"

    invoices_count = fields.Integer(compute="_compute_invoices_count",
                                    string="# of invoices", default=0)

    def _compute_invoices_count(self):
        Invoice_obj = self.env["invoice.invoice"]
        # Attemp with search
        count = 0
        for partner in self:
            count += Invoice_obj.search_count(
                [("partner_id", "=", partner.id)])
        self.invoices_count = count

    def action_window_btn(self):
        obj = {
            "type": "ir.actions.act_window",
            "name": "invoice state",
            "res_model": "invoice.invoice",
            "views": [[False, "tree"], [False, "form"]],
            "domain": [["partner_id", "=", self.id]],
        }
        return obj
