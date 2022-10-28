# -*- coding: utf-8 -*-
# from odoo import http


# class FixSendEmail(http.Controller):
#     @http.route('/fix_send_email/fix_send_email/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fix_send_email/fix_send_email/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fix_send_email.listing', {
#             'root': '/fix_send_email/fix_send_email',
#             'objects': http.request.env['fix_send_email.fix_send_email'].search([]),
#         })

#     @http.route('/fix_send_email/fix_send_email/objects/<model("fix_send_email.fix_send_email"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fix_send_email.object', {
#             'object': obj
#         })
