# -*- coding: utf-8 -*-
from unicodedata import category
from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale

import logging

log = logging.getLogger(__name__)


class WebsiteCustomJs(WebsiteSale):

    def check_limit_category(self, user_id, add_qty, product_id):
        product_category_id = http.request.env['product.product'].browse(
            int(product_id)).categ_id.id
        category_limit = http.request.env['category.limit'].search([
            ('partner_id', '=', user_id),
            ('category_id', '=', product_category_id)
        ], limit=1)
        if int(add_qty) >= category_limit.limit or (int(add_qty) + category_limit.quantity_consumed) >= category_limit.limit:
            return http.request.render("website_custom_js.add_cart_limited_category", {})

    def check_limit_quantity(self, user_id, add_qty, product_id):
        product_limit = http.request.env['product.limit'].search([
            ('partner_limit', '=', user_id),
            ('product.id', '=', int(product_id))
        ])

        if int(add_qty) >= product_limit.limit or (int(add_qty) + product_limit.quantity_consumed) >= product_limit.limit:
            return http.request.render("website_custom_js.add_cart_limited_quantity", {})

    @http.route(['/shop/cart/update'], type='http', auth="public", methods=['GET', 'POST'], website=True, csrf=False)
    def cart_update(self, product_id, add_qty=1, set_qty=0, **kw):
        user = http.request.env.context.get('uid')
        user_id = http.request.env['res.users'].browse(int(user)).partner_id.id
        website_obj = http.request.website

        if website_obj.is_limit_product:
            self.check_limit_quantity(user_id, add_qty, product_id)
        else:
            self.check_limit_category(user_id, add_qty, product_id)

        return super(WebsiteCustomJs, self).cart_update(product_id, add_qty, set_qty)
