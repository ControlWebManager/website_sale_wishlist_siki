# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import openerp
import re
from openerp import models, api, fields

class ViewStatus(models.Model):
    _inherit = 'website'

    #value_field_active_view = fields.Boolean(compute='_compute_active_view', store=False)
    """
    @api.model
    def _compute_active_view(self):
        self.ensure_one()
        self.env.cr.execute("SELECT active FROM ir_ui_view WHERE key='website_sale.products_list_view'")
        value = self.env.cr.fetchone()[0]
        self.value_field_active_view = value

        return True"""
    @api.model
    def _compute_website_view(self):
        self.ensure_one()
        self.env.cr.execute("SELECT active FROM ir_ui_view WHERE key='website_sale.products_list_view'")
        value = self.env.cr.fetchone()[0]
        # self.value_field_active_view = value
        return value