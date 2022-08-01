# -*- coding: utf-8 -*-
{
    'name': "sale_report",

    'summary': """
        Reporte en ventas
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "ArobyR",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/paper_format.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/res_company_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
