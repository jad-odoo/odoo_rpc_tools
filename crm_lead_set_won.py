# -*- coding: utf-8 -*-
import sys

from odoo_csv_tools.lib import conf_lib
from odoo_csv_tools.lib.internal.rpc_thread import RpcThread
from files import *
from prefix import *
import math

connection = conf_lib.get_server_connection(config_file)
model_data = connection.get_model('ir.model.data')
model_crm_lead = connection.get_model('crm.lead')

data_recs = model_data.search_read([('module', '=', CRM_LEAD_PREFIX), ('model', '=', 'crm.lead')], ['res_id'])

lead_ids = []
for rec in data_recs:
    lead_ids.append(rec['res_id'])

crm_lead_ids = model_crm_lead.search([('id', 'in', lead_ids)])

print 'Leads to set as WON: %s' % len(crm_lead_ids)

# def chunks(var_list, chunk_size):
#     for i in range(0, len(var_list), chunk_size):
#         yield var_list[i:i+chunk_size]

# chunck_size = 10
# i = 1
# crm_lead_chunks = list(chunks(crm_lead_ids, chunck_size))
# run_count = int(math.ceil(len(crm_lead_ids) / chunck_size) + 1)
# for chunk in crm_lead_chunks:
#     print 'Process chunk %s of %s' % (i, run_count)
#     model_crm_lead.action_set_won(chunk)
#     i += 1

for rec in crm_lead_ids:
    print 'Mark lead %s as won' % rec
    model_crm_lead.action_set_won_rainbowman(rec)


