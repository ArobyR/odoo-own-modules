# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    account_journal_id = fields.Many2one('account.journal', string='Diario')
