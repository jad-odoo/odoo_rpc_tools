# -*- coding: utf-8 -*-
import sys
from odoo_csv_tools.lib import conf_lib
from odoo_csv_tools.lib.internal.rpc_thread import RpcThread
from files import *
from prefix import *
import math


connection = conf_lib.get_server_connection(config_file)
model_data = connection.get_model('ir.model.data')
model_invoice = connection.get_model('account.invoice')

data_recs = model_data.search_read([('module', '=', VENDOR_BILL_PREFIX), ('model', '=', 'account.invoice')], ['res_id'])

invoice_ids_all = []
for rec in data_recs:
    invoice_ids_all.append(rec['res_id'])

print 'Invoices imported: %s' % len(invoice_ids_all)

invoice_ids = model_invoice.search([('id', 'in', invoice_ids_all), ('amount_tax', '=', 0)])

print 'Invoices to compute: %s' % len(invoice_ids)

def chunks(var_list, chunk_size):
    for i in range(0, len(var_list), chunk_size):
        yield var_list[i:i+chunk_size]

chunck_size = 20
i = 1
invoice_chunks = list(chunks(invoice_ids, chunck_size))
run_count = int(math.ceil(len(invoice_ids) / chunck_size) + 1)
for chunk in invoice_chunks:
    print 'Process chunk %s of %s' % (i, run_count)
    model_invoice.compute_taxes(chunk)
    i += 1


