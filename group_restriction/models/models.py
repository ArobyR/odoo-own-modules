# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class group_restriction(models.Model):
#     _name = 'group_restriction.group_restriction'
#     _description = 'group_restriction.group_restriction'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
