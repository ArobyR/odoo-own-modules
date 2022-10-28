# -*- coding: utf-8 -*-
# from odoo import http


# class SummaryQuantities(http.Controller):
#     @http.route('/summary_quantities/summary_quantities/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/summary_quantities/summary_quantities/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('summary_quantities.listing', {
#             'root': '/summary_quantities/summary_quantities',
#             'objects': http.request.env['summary_quantities.summary_quantities'].search([]),
#         })

#     @http.route('/summary_quantities/summary_quantities/objects/<model("summary_quantities.summary_quantities"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('summary_quantities.object', {
#             'object': obj
#         })
