# -*- coding: utf-8 -*-



{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'author': 'Nirooba',
    'website': 'https://nirooba.com',
    'sequence': -100,
    'category': 'Hospital',
    'summary': 'Hostpital management system',
    'description': """Hostpital management system """,
    'depends': ['mail'],
    'data': ['views/menu.xml',
             'views/patient.xml',
             'security/ir.model.access.csv',
             'views/female_patient.xml',
             'views/appointment_view.xml'],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}
