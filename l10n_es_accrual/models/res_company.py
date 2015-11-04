# -*- coding: utf-8 -*-
# (c) 2015 Antiun Ingeniería S.L. - Pedro M. Baeza
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    def _default_default_prepaid_revenue_account_id(self):
        return self.env['account.account'].search(
            [('code', 'like', '48500%'),
             ('company_id', '=', self.id)])

    def _default_default_prepaid_expense_account_id(self):
        return self.env['account.account'].search(
            [('code', 'like', '48000%'),
             ('company_id', '=', self.id)])

    default_prepaid_revenue_account_id = fields.Many2one(
        default=_default_default_prepaid_revenue_account_id)
    default_prepaid_expense_account_id = fields.Many2one(
        default=_default_default_prepaid_expense_account_id)
