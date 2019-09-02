# -*- coding: utf-8 -*-

import openerplib
from datetime import datetime
from prefix import *
from files import *
from libfunc import *
from odoo_csv_tools.lib import conf_lib

connection = conf_lib.get_server_connection(config_file)

connection.check_login()

model_account_move = connection.get_model('account.move')
model_data = connection.get_model('ir.model.data')

company_id = get_company_id(COMPANY_ID_3, connection)

journal_id = get_journal_id(connection, ACCOUNT_JOURNAL_PREFIX_3)

move_name = get_open_move_name(COMPANY_ID_3, connection, ACCOUNT_JOURNAL_PREFIX_3)

account_move_res_id = model_account_move.create({
    'name': move_name,
    'journal_id': journal_id,
    'date': datetime.strptime("12/31/2017", "%m/%d/%Y").strftime("%Y-%m-%d 00:00:00"),
    'ref': "Balance d'ouverture au 2018",
})

print account_move_res_id

model_data.create({
    'module': ACCOUNT_MOVE_PREFIX_3,
    'name': 'OPDIV_%s' % move_name,
    'model': 'account.move',
    'res_id': account_move_res_id,
})

