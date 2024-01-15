# -*- coding: utf-8 -*-
# from odoo import http


# class AlertCreditLimit(http.Controller):
#     @http.route('/alert_credit_limit/alert_credit_limit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alert_credit_limit/alert_credit_limit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('alert_credit_limit.listing', {
#             'root': '/alert_credit_limit/alert_credit_limit',
#             'objects': http.request.env['alert_credit_limit.alert_credit_limit'].search([]),
#         })

#     @http.route('/alert_credit_limit/alert_credit_limit/objects/<model("alert_credit_limit.alert_credit_limit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alert_credit_limit.object', {
#             'object': obj
#         })
