# -*- coding: utf-8 -*-
import sys
import openerplib
from prefix import *
from files import *
from odoo_csv_tools.lib import conf_lib
from odoo_csv_tools.lib.internal.rpc_thread import RpcThread
from openerplib.main import JsonRPCException

connection = conf_lib.get_server_connection(config_file)
                                      
connection.check_login()

model_account_move = connection.get_model("account.move")
model_data = connection.get_model('ir.model.data')

# Get all id of imported account.move
data_ids = model_data.search([('module', '=', ACCOUNT_MOVE_PREFIX_2), ('model', '=', 'account.move')])
records = model_data.read(data_ids, ['res_id'])
record_ids = []
for rec in records:
    record_ids.append(rec['res_id'])

# Get unposted account.move
am_ids = model_account_move.search([('id', 'in', record_ids), ('state', '=', 'draft')])

print 'Posting %s account.move' % len(am_ids)

rpc_thread = RpcThread(4)

for record in am_ids:
    print 'Posting account.move %s' % record
    try :
        rpc_thread.spawn_thread(model_account_move.action_post, [record])
    except JsonRPCException as e:
        print 'Traceback: %s' % e
        pass

print 'Done.'