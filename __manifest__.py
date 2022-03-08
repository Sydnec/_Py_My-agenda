# -*- coding: utf-8 -*-
{
    'name': "My agenda",

    'summary': """
        Ajout de RDV sur agenda d'une personne
        Récupération personne, agenda, libre, ...""",

    'description': """
        Long description of module's purpose
    """,

    'author': "gr3-22",
    'website': "https://github.com/Sydnec/_Py_My-agenda",

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
        'views/my-agenda.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}