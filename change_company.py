# -*- coding: utf-8 -*-
import sys
import openerplib
from prefix import *
from files import *
from odoo_csv_tools.lib import conf_lib

connection = conf_lib.get_server_connection(config_file)

model_user = connection.get_model("res.users")
model_company = connection.get_model("res.company")

user = model_user.search([('id', '=', 2)])

# company_id = sys.argv[1]
# company = model_company.search_read([('id', '=', company_id)], ['id', 'name'])

company_name = sys.argv[1]
company = model_company.search_read([('name', '=', company_name)], ['id', 'name'])


if not len(company):
    print 'Company not found'
else:
    res = model_user.write(user, {'company_id': company[0]['id']})
    if res: 
        print 'Admin company set to: %s' % company[0]['name']
    else:
        print 'Cannot set admin company'
