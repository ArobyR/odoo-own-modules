# -*- coding: utf-8 -*-
# from odoo import http


# class QwebReportModule(http.Controller):
#     @http.route('/qweb_report_module/qweb_report_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qweb_report_module/qweb_report_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qweb_report_module.listing', {
#             'root': '/qweb_report_module/qweb_report_module',
#             'objects': http.request.env['qweb_report_module.qweb_report_module'].search([]),
#         })

#     @http.route('/qweb_report_module/qweb_report_module/objects/<model("qweb_report_module.qweb_report_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qweb_report_module.object', {
#             'object': obj
#         })
