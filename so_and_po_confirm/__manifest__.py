# -*- coding: utf-8 -*-
{
    'name': "Confirm s0 p0",

    'summary': """
        Create wizards for be the first step for confirm S0 and P0 document.
    """,

    'description': """
        Create wizards for be the first step for confirm S0 and P0 document.
    """,

    'author': "ArobyR",
    'website': "http://www.growit.com.do/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
