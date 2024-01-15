# -*- coding: utf-8 -*-

from odoo import models, fields


class WizardSaleAlert(models.TransientModel):
    _name = 'wizard.sale.alert'

    def active_is_authorized_confirm(self):
        sale_id = self.env.context.get('active_id', 0)

        sale_obj = self.env['sale.order'].browse(sale_id)

        if sale_obj:
            sale_obj.is_authorized_confirm = True
