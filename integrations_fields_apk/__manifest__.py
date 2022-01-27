# -*- coding: utf-8 -*-
{
    'name': "Integracion con apk",

    'summary': """
       Integracion con apk""",

    'description': """
        Integracion con apk
    """,

    'author': "Ronny Montano",
    'website': "",
    'category': 'developers',
    'version': '0.1',

    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_invoice.xml',
    ],

    "application": False,
    "installable": True,
    "auto_install": False,
}