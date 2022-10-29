# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging

_log = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    
    def open_purchase_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Confirmar orden.",
            "res_model": "purchase.confirm",
            "views": [[False, "form"]],
            "view_id": self.env.ref('so_and_po_confirm.view_purchase_confirm').id,
            "target": "new",
        }
    

class PurchaseConfirm(models.TransientModel):
    _name = 'purchase.confirm'
    
    def confirm_purchase_order(self):
        active_id =  self.env.context.get('active_id')
        purchase_object = self.env['purchase.order'].search(
            [('id', '=', active_id)]
        )
        
        _log.error(active_id)
        _log.error(purchase_object)
        
        if len(purchase_object):
            purchase_object.button_confirm()
        
        return 


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def open_sale_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": "Confirmar Venta.",
            "res_model": "sale.confirm",
            "views": [[False, "form"]],
            "view_id": self.env.ref('so_and_po_confirm.view_sale_confirm').id,
            "target": "new",
        }    

    
class SaleOrderConfirm(models.TransientModel):
    _name = 'sale.confirm'
    
    def confirm_sale_order(self):
        active_id =  self.env.context.get('active_id')
        sale_order_object = self.env['sale.order'].search(
            [('id', '=', active_id)]
        )
        
        if len(sale_order_object):
            sale_order_object.action_confirm()
        
        return         