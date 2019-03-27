# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import openerp
import re
import logging

from openerp import models, api, fields
from openerp.exceptions import ValidationError

_logger = logging.getLogger(__name__)




class ViewStatus(models.Model):
    _inherit = 'website'

    #value_field_active_view = fields.Boolean(compute='_compute_active_view', store=False)

    @api.multi
    def _compute_website_view_wishlist(self):
        recordset = self.env['ir.ui.view']
        form_List = recordset.search([('key', '=', 'website_sale.products_list_view')])

        Productsitem = recordset.search([('key', '=', 'website_sale.products_item')])

        #AddtoCart inherit Productsitem
        AddtoCart = recordset.search([('key', '=', 'website_sale.products_add_to_cart')])

        #Extension

        AddtoCartwithEase = recordset.search([('key','=','add_to_cart.products_item_inherited')])

        AddtoWishlistFromList = recordset.search([('key','=','website_sale_wishlist.products_add_to_wishlist')])

        AddtoWishlistFromListExtend = recordset.search([('key', '=', 'website_sale_wishlist_siki.products_add_to_wishlist_extend')])

        for record in AddtoWishlistFromList:

            if record.active == True:
                #print('Con info si', AddtoWishlistFromList.id)
                AddtoCartwithEase.active = True
                #   AddtoCartwithEase.customize_show = False
                self.ensure_one()

        return True

    @api.multi
    def _list_add_cart(self):
        value = self._compute_website_view()
        if value == 'top_right':
            return 'float: right;margin-top: 5px;margin-right:2%; z-index: 999;position: relative;'
        if value == 'list_add_cart':
            return 'float: right;clear: both;'

    @api.model
    def active_view(self):
        recordset = self.env['ir.ui.view']
       # raise ValidationError("A session's instructor can't be an attendee")
        #AddtoCartwithEase = recordset.search([('key', '=', 'add_to_cart.products_item_inherited')])


        try:
            print('try')
            self.env.cr.execute("UPDATE ir_ui_view SET active= %s WHERE key= %s",
                                (True, 'add_to_cart.products_item_inherited',))
            self.env.cr.execute("SELECT id FROM ir_ui_view WHERE key= %s", ('add_to_cart.products_item_inherited',))
            value = self.env.cr.fetchone()[0]
            return value
        except Exception:
            print('exeption')
            return False
