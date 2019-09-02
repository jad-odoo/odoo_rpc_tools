# -*- coding: utf-8 -*-

# NOT USED

import openerplib
from prefix import *

connection = openerplib.get_connection(hostname=HOST, 
                                       port=PORT, 
                                       database=DATABASE,
                                       login=LOGIN, 
                                       password=PASSWORD, 
                                       protocol=PROTOCOL,
                                       user_id=USERID)
                                       
connection.check_login()

model_account = connection.get_model('account.account')
model_data = connection.get_model('ir.model.data')

accounts = model_account.search_read([('company_id', '!=', 1)], ['id', 'code', 'company_id'])

for account in accounts:
    print '%s %s %s' % (account['id'], account['code'], account['company_id'])

    # Retreive company_id from account['company_id']
    company_names = model_data.search_read([('res_id', '=', account['company_id']), ('model', '=', 'res.company')], ['name'], limit=1)
    company_id_xml = company_names[0]['name']

    module = 'sodaphi_company%s_account_account' % company_id_xml

    rec_count = model_data.search_count([('model', '=', 'account.account'), ('res_id', '=', account['id'])])
    # print rec_count
    
    if not rec_count:
    # Create account.account XML_ID
        account_data_id = model_data.create({
            'module': module,
            'name': account['code'],
            'model': 'account.account',
            'res_id': account['id'],
        })

        print 'Created id: %s' % account_data_id

