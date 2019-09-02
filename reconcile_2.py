# -*- coding: utf-8 -*-

import openerplib
from prefix import *
from files import *
from odoo_csv_tools.lib import conf_lib
from libfunc import *
from odoolib import *

connection = conf_lib.get_server_connection(config_file)
                                       
connection.check_login()
model_account_move_line = connection.get_model('account.move.line')
model_data = connection.get_model('ir.model.data')

company_id = get_company_id(COMPANY_ID_2, connection)

recs = model_account_move_line.search_read([('matchno', '!=', False), ('company_id', '=', company_id)], ['matchno'])

matchnos = []
for rec in recs:
    matchnos.append(rec['matchno'])

matchnos = list(set(matchnos))

for matchno in matchnos:
    print 'Reconcile matchno %s' % matchno
    recs = model_account_move_line.search([('matchno', '=', matchno)])
    
    # Print move line XML_ID for debug
    ids = model_data.search_read([('module', '=', ACCOUNT_MOVE_LINE_PREFIX_2), ('model', '=', 'account.move.line'), ('res_id', 'in', recs)], ['module', 'name'])
    for id in ids:
        print '\t%s' % id['name']

    try:
        res = model_account_move_line.reconcile(recs)
        print res
    except JsonRPCException as e:
        print e
        pass

