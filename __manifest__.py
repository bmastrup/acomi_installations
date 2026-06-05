{
    'name': "Anlæg",
    'depends': [
        'base',
        'mail',
        'planning',
        'sale',
    ],
    'application': True,
    'author': "Acomi",
    'license': "LGPL-3",
    'data': [
        'security/ir.model.access.csv',
        'views/acomi_installation_views.xml',
        'views/sale_order_views.xml',
        'views/acomi_installation_type_views.xml',
        'views/acomi_installation_menus.xml',
    ]

}
