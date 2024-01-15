# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_authorized_confirm = fields.Boolean()

    def action_confirm(self):

        if (self.partner_id.credit >= self.partner_id.credit_limit and
                self.partner_id.use_partner_credit_limit and self.is_authorized_confirm is False):
            return {
                "type": "ir.actions.act_window",
                "name": "Alerta: limite de credito.",
                "res_model": "wizard.sale.alert",
                "views": [[False, "form"]],
                "view_id": self.env.ref('alert_credit_limit.view_wizard_sale_alert').id,
                "target": "new",
            }

        return super(SaleOrder, self).action_confirm()

    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).

        Override method
        """
        self.ensure_one()

        res = super(SaleOrder, self)._prepare_invoice()
        # add the new field
        res['is_authorized_confirm'] = self.is_authorized_confirm,
        return res


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_authorized_confirm = fields.Boolean()

    def action_post(self):
        if (self.partner_id.credit >= self.partner_id.credit_limit and
                self.partner_id.use_partner_credit_limit and self.is_authorized_confirm is False):
            return {
                "type": "ir.actions.act_window",
                "name": "Alerta: limite de credito.",
                "res_model": "wizard.invoice.alert",
                "views": [[False, "form"]],
                "view_id": self.env.ref('alert_credit_limit.view_wizard_invoice_alert').id,
                "target": "new",
            }

        return super(AccountMove, self).action_post()
