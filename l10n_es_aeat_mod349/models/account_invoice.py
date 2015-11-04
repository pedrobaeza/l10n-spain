# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields, api, exceptions, _

OPERATION_KEYS = [
    ('E', 'E - Intra-Community supplies'),
    ('A', 'A - Intra-Community acquisition'),
    ('T', 'T - Triangular operations'),
    ('S', 'S - Intra-Community services'),
    ('I', 'I - Intra-Community services acquisitions'),
    ('M', 'M - Intra-Community supplies without taxes'),
    ('H', 'H - Intra-Community supplies without taxes '
     'delivered by legal representative')
]


class AccountInvoice(models.Model):
    """Inheritance of account invoce to add some fields:
    - operation_key: Operation key of invoice
    """
    _inherit = 'account.invoice'

    def _get_operation_key(self, fp, invoice_type):
        if not fp.intracommunity_operations:
            return False
        else:
            # TODO: Ver cómo discernir si son prestación de servicios
            if invoice_type in ('out_invoice', 'out_refund'):
                # Establecer a entrega si es de venta
                return 'E'
            else:
                # Establecer a adquisición si es de compra
                return 'A'

    def _get_year_from_fy_month(self, fy, month):
        fy_start = fields.Date.from_string(fy.date_start)
        fy_stop = fields.Date.from_string(fy.date_stop)
        if fy_start.month < month:
            year = fy_start.year
        elif fy_stop.month > month:
            year = fy_stop.year
        else:
            raise exceptions.Warning(
                _('Cannot get invoices.\nProvided month is not included on '
                  'selected fiscal year'))
        return year

    @api.model
    def _get_invoices_by_type(self, partner, operation_key, periods=None):
        """
        Returns invoices ids by type (supplier/customer) for a fiscal
        year, period or month.
        """
        # Set type of invoice
        invoice_type = ('in_invoice', 'out_invoice', 'in_refund', 'out_refund')
        domain = [('partner_id', 'child_of', partner.id),
                  ('state', 'in', ['open', 'paid']),
                  ('type', 'in', invoice_type),
                  ('operation_key', '=', operation_key)]
        if periods:
            domain.append(('period_id', 'in', periods.ids))
        return self.search(domain)

    @api.multi
    def clean_refund_invoices(self, periods=None):
        """Separate refunds from invoices"""
        invoices = self.env['account.invoice']
        refunds = self.env['account.invoice']
        for inv in self:
            if inv in ('in_refund', 'out_refund'):
                if not inv.origin_invoices_ids:
                    invoices += inv
                    continue
                for origin_line in inv.origin_invoices_ids:
                    if origin_line.state in ('open', 'paid'):
                        if origin_line.period_id not in periods:
                            refunds += inv
                        else:
                            invoices += inv
            else:
                invoices += inv
        return invoices, refunds

    @api.multi
    def on_change_fiscal_position(self, fiscal_position, invoice_type):
        """Suggest an operation key when fiscal position changes."""
        res = {'operation_key': False}
        if fiscal_position and invoice_type:
            fp = self.env['account.fiscal.position'].browse(fiscal_position)
            res['operation_key'] = self._get_operation_key(fp, invoice_type)
        return {'value': res}

    @api.model
    def create(self, vals):
        """Writes operation key value, if invoice is created in
        backgroud with intracommunity fiscal position defined"""
        if vals.get('fiscal_position') and \
                vals.get('type') and not vals.get('operation_key'):
            fp_obj = self.env['account.fiscal.position']
            fp = fp_obj.browse(vals['fiscal_position'])
            vals['operation_key'] = self._get_operation_key(fp, vals['type'])
        return super(AccountInvoice, self).create(vals)

    operation_key = fields.Selection(selection=OPERATION_KEYS,
                                     string='Operation key')
