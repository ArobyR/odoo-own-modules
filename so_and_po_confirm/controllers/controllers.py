# -*- coding: utf-8 -*-
# from odoo import http


# class SoAndPoConfirm(http.Controller):
#     @http.route('/so_and_po_confirm/so_and_po_confirm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/so_and_po_confirm/so_and_po_confirm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('so_and_po_confirm.listing', {
#             'root': '/so_and_po_confirm/so_and_po_confirm',
#             'objects': http.request.env['so_and_po_confirm.so_and_po_confirm'].search([]),
#         })

#     @http.route('/so_and_po_confirm/so_and_po_confirm/objects/<model("so_and_po_confirm.so_and_po_confirm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('so_and_po_confirm.object', {
#             'object': obj
#         })
