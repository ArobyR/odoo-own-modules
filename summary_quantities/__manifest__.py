# -*- coding: utf-8 -*-
{
    'name': "summary quantities",

    'summary': """
        Summary of quantities in Sale
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "ArobyR",
    'website': "http://www.github.com/ArobyR",
    'company': "GrowIT",

    'category': 'Sale',
    'version': '0.1',

    'depends': ['base', 'sale'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
