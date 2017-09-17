# -*- coding: utf-8 -*-
{
    'name': "tiendo_optimalpurchase",

    'summary': """
        Enhancing supplier selection by making optimized PurchaseOrders using linear programming""",

    'description': """
        This module tries to improve Odoos PurchaseOrder generation by using linear programming. 
        Linear programming is a easy way for defining combinatorial problems, such as the Knappsack problem. 
        The Knappsack problem could be utilized to select the set suppliers a ProcurementOrder should be bought of. 
        For technical implementation the lpSolve-Solver shall be used.
    """,

    'author': "tiendo GmbH",
    'website': "http://www.tiendo.de",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Purchases',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'tiendo_smartpurchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}