# -*- coding: utf-8 -*-
{
    'name': 'PageLanding',
    'description':
        """
            Descubre como puedes administrar tu negocio como las grandes empresas. 
            Controla tus ventas, precios e inventario con tu plataforma 100% web, 
            desde cualquier lugar.
        """,

    'summary': 'Tu Comercio en un Dia',
    'author': 'José Ramón Vidal Wilson',
    'website': "https://tcm.geztion.pro/",

    'category': 'TCM',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'demo.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/landing_view.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
       # 'demo.xml',
    ],
    'qweb': [
        # 'static/src/xml/treeview_button_importar_orden.xml',
        # 'static/src/xml/web_ir_actions_act_window_message.xml',
    ],
}