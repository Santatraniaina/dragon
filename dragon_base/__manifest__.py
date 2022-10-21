# -*- coding: utf-8 -*-
{
    'name': "dragon_base",

    'summary': """
        Dragon module for practise""",

    'description': """
        This is a sample practise to initiate Odoo and take example of Student Management for practising
    """,

    'author': "KASIA",
    'website': "http://www.kasia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/student_base_views.xml',
        'views/student_class_views.xml',
        'views/res_partner_views.xml',
        'views/templates.xml',
        'data/student_base_sequence.xml',
        'data/student_class_sequence.xml',
    ],
    # only loaded in demonstration modes
    'demo': [
        'demo/demo.xml',
    ],
}
