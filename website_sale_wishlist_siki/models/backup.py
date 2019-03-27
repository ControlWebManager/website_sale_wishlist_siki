# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import openerp
import re
from openerp import models, api, fields

class ViewStatus(models.Model):
    _inherit = 'website'

    #value_field_active_view = fields.Boolean(compute='_compute_active_view', store=False)

    @api.model
    def _compute_website_view(self):

        recordset = self.env['ir.ui.view']
        form_List = recordset.search([('key', '=', 'website_sale.products_list_view')])

        Productsitem = recordset.search([('key', '=', 'website_sale.products_item')])

        #AddtoCart inherit Productsitem
        AddtoCart = recordset.search([('key', '=', 'website_sale.products_add_to_cart')])

        #Extension
        AddtoCartwithEase = recordset.search([('key','=','add_to_cart.products_item_inherited')])

        AddtoWishlistFromList = recordset.search([('key','=','website_sale_wishlist.products_add_to_wishlist')])
        print(AddtoWishlistFromList.active)
        if AddtoWishlistFromList.active:
            print('estoy activado',AddtoCart.customize_show,AddtoCartwithEase.customize_show)
            AddtoCart.customize_show = False
            AddtoCartwithEase.customize_show = False
        else:
            AddtoCart.customize_show = True


        return True

    def _list_add_cart(self):
        value = self._compute_website_view()
        if value == 'top_right':
            return 'float: right;margin-top: 5px;margin-right:2%; z-index: 999;position: relative;'
        if value == 'list_add_cart':
            return 'float: right;clear: both;'


# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import openerp
import re
from openerp import models, api, fields

from openerp.exceptions import ValidationError


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

           """ if record.active == True:
                print('Con info si', AddtoWishlistFromList.id)
                AddtoCartwithEase.active = True
                AddtoCartwithEase.customize_show = False
                self.ensure_one()"""

        return True

    def _list_add_cart(self):
        value = self._compute_website_view()
        if value == 'top_right':
            return 'float: right;margin-top: 5px;margin-right:2%; z-index: 999;position: relative;'
        if value == 'list_add_cart':
            return 'float: right;clear: both;'