# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Module WebSite Sale wishlist',
    'summary': 'Child Module - Parent website_sale_wishlist',
    'version': '1.0',
    'author' : 'SIKI SAS, Developer Ing Henry Vivas',
	'website' : 'www.sikisoftware.com',
    "support": "controlwebmanager@gmail.com",
    'category': 'Website',
    'description': """
This module extend module WebSite Sal Wishlist.
========================================================================

List of modifications:
-------------------
    * V.-1.0 Position icon wishlist Top - Right ( Req. 10 )
    * V.-1.1 Desing Css Title Description and Features
    * V.-1.2 Best structu Code Python in Model and Xml, More eficcient
*Require
    * This module to work needs the installation of the add_to_cart_siki module 
 """,
    'data': [
        'data/data.xml',
        'views/shop.xml',

    ],
    'depends': [
        'base',
        'website',
        'website_sale',
        'website_sale_wishlist',
        'add_to_cart',
        'add_to_cart_siki',
    ],
    'installable': True,
    'application': False,
}