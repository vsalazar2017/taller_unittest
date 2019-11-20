# -*- coding: utf-8 -*-
{
    'name': "Odoo unit test",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Trescloud",
    'website': "https://www.trescloud.com/",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/todo_menu.xml',
        'views/view_alumno.xml',
        'views/view_curso.xml',
        'views/view_dictar.xml',
        'views/view_matricula.xml',
        'views/view_notas.xml',
        'views/view_profesor.xml',
    ],
    'demo': [
    ],
}