# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inherited_module(models.Model):
    _inherit = 'invoice.invoice'

    partner = fields.Many2one("res.partner", string="Partner")

    def inherited_action(self):
        link = self.env["account.move"].create({
                "partner_id": self.partner.id,
                "invoice_date": self.date_invoice,
                "invoice_line_ids": self._get_products_formatted(),
                "move_type": "out_invoice",
            })
        self.invoice_generated = link.id


