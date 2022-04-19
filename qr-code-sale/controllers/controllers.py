# -*- coding: utf-8 -*-
# from odoo import http


# class Qr-code-sale(http.Controller):
#     @http.route('/qr-code-sale/qr-code-sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qr-code-sale/qr-code-sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qr-code-sale.listing', {
#             'root': '/qr-code-sale/qr-code-sale',
#             'objects': http.request.env['qr-code-sale.qr-code-sale'].search([]),
#         })

#     @http.route('/qr-code-sale/qr-code-sale/objects/<model("qr-code-sale.qr-code-sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qr-code-sale.object', {
#             'object': obj
#         })
