# -*- coding: utf-8 -*-
import sys

from odoo_csv_tools.lib import conf_lib
from odoo_csv_tools.lib.internal.rpc_thread import RpcThread
from files import *
from prefix import *
import math

connection = conf_lib.get_server_connection(config_file)
model_data = connection.get_model('ir.model.data')
model_users = connection.get_model('res.users')

data_recs = model_data.search_read([('module', '=', RES_USERS_PREFIX), ('model', '=', 'res.users')], ['res_id'])

user_ids = []
for rec in data_recs:
    user_ids.append(rec['res_id'])


users = model_users.search([('id', 'in', user_ids), ('id', '>', 2), ('name', 'not in', ['TIM', 'ANN'])])
print 'Archiving %s users' % len(users)
model_users.write(users, {'active': False})