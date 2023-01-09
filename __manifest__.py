# -*- coding: utf-8 -*-
{
    'name': "Exam_Management",

    'summary': """
        Practice task of Daffodil International University""",

    'description': """
        This module is for for Training practice task of Daffodil International University
    """,

    'author': "DCL",
    'website': "https://daffodil-bd.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Management System',
    
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/studentinfo.xml',
        'views/studentresult.xml',
        'views/menus.xml',
    ],
    
}
