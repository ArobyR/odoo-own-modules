# -*- coding: utf-8 -*-
# from odoo import http


# class ProductSale(http.Controller):
#     @http.route('/product_sale/product_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_sale/product_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_sale.listing', {
#             'root': '/product_sale/product_sale',
#             'objects': http.request.env['product_sale.product_sale'].search([]),
#         })

#     @http.route('/product_sale/product_sale/objects/<model("product_sale.product_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_sale.object', {
#             'object': obj
#         })
