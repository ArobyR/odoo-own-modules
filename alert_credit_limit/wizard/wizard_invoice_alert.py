# -*- coding: utf-8 -*-

from odoo import models, fields


class WizardInvoiceAlert(models.TransientModel):
    _name = 'wizard.invoice.alert'

    def active_is_authorized_confirm(self):
        invoice_id = self.env.context.get('active_id', 0)

        invoice_obj = self.env['account.move'].browse(invoice_id)

        if invoice_obj:
            invoice_obj.is_authorized_confirm = True
