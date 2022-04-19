# -*- coding: utf-8 -*-
# from odoo import http


# class GroupRestriction(http.Controller):
#     @http.route('/group_restriction/group_restriction/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/group_restriction/group_restriction/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('group_restriction.listing', {
#             'root': '/group_restriction/group_restriction',
#             'objects': http.request.env['group_restriction.group_restriction'].search([]),
#         })

#     @http.route('/group_restriction/group_restriction/objects/<model("group_restriction.group_restriction"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('group_restriction.object', {
#             'object': obj
#         })
