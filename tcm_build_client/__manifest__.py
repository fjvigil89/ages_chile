# -*- coding: utf-8 -*-
{
    'name': 'TCM Build Client',
    'description':
        """
            Construye una instancia cliente de TCM basado
            en un plan seleccionado por el cliente,
            servicios adicionales y medios de pago.
        """,

    'summary': 'Tu Comercio en un Dia',
    'author': 'José Ramón Vidal Wilson',
    'website': "https://tcm.geztion.pro/",

    'category': 'TCM',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'application': False,
    'installable': True,
    'auto_install': False,
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'demo.xml',
        # 'security/ir.model.access.csv',
        'views/webclient_templates.xml',
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