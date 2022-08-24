# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
	'name' : "Hospital Management",
	'version' : '1.0',
	'summary': "hospital management",
	'sequence': 10,
    'author': "By D3V",
	'description': """hospital management""",
	'category': "extra tools",
	'website': "https://www.google.com",    
	'depends' : ['base'],
	'images': ['static/description/icon.jpeg'],
	'data': [
	'security/ir.model.access.csv',
	'views/hospital_view.xml',
	],
	'installable': True,
	'application': True,
	'license': 'LGPL-3',
}
