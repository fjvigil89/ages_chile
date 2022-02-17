# -*- coding: utf-8 -*-
{
    'name': "ACCESO CLIENTES",

    'summary': """
        interface to login users""",

    'description': """
       
    """,

    'author': "Ronny Montano <<rmontano1992@gmail.com>>",
    'category': 'Others',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'web'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/access_client_menu.xml',
        'views/user_distribution_database.xml',
        # 'views/templates.xml',
        # 'views/res_partner_views.xml',
        # 'views/product_product_view.xml',
        # 'views/training_consult_view.xml',
        # 'views/maestras_view.xml',
    ],
}
