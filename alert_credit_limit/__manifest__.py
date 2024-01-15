# -*- coding: utf-8 -*-
{
    'name': "alert_credit_limit",
    'summary': """
        Alert credit limit in SO and BILL
        """,
    'description': """
    """,
    'author': "ArobyR",
    'website': "https://www.github.com/ArobyR",
    'license': 'LGPL-3',
    'category': 'Alert',
    'version': '1.2',
    'depends': ['sale', 'account'],
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'wizard/wizard_sale_alert_views.xml',
        'wizard/wizard_invoice_alert_views.xml',
    ],
}
