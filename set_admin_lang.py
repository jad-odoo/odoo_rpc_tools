# -*- coding: utf-8 -*-
import sys
import openerplib
from prefix import *
from files import *
from odoo_csv_tools.lib import conf_lib

connection = conf_lib.get_server_connection(config_file)

model_partner = connection.get_model("res.partner")

user = model_partner.search([('name', '=', 'Administrator')])

lang = sys.argv[1]


if not len(user):
    print 'Administrator partner not found'
else:
    admin_name = 'TIM'
    res = model_partner.write(user, {'name': admin_name, 'lang': lang})
    if res: 
        print 'Admin name is now %s, language set to: %s' % (admin_name, lang)
    else:
        print 'Cannot setup Admin partner'
