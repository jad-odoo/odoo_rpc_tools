# -*- coding: utf-8 -*-
import sys

from odoo_csv_tools.lib import conf_lib
from odoo_csv_tools.lib.internal.rpc_thread import RpcThread
from files import *
from prefix import *
import math

connection = conf_lib.get_server_connection(config_file)
model_data = connection.get_model('ir.model.data')
model_purchase_order = connection.get_model('purchase.order')
model_stock_picking = connection.get_model('stock.picking')

data_recs = model_data.search_read([('module', '=', PURCHASE_ORDER_PREFIX), ('model', '=', 'purchase.order')], ['res_id'])

po_ids = []
for rec in data_recs:
    po_ids.append(rec['res_id'])

pos = model_purchase_order.search_read([('id', 'in', po_ids)], ['picking_ids'])

stock_picking_ids = []
for po in pos:
    stock_picking_ids.extend(po['picking_ids'])

stock_picking_ids = list(set(stock_picking_ids))

print 'Stock picking to remove: %s' % len(stock_picking_ids)
# print stock_picking_ids

# model_stock_picking.unlink(stock_picking_ids[:len(stock_picking_ids)/2])
# model_stock_picking.unlink(stock_picking_ids[len(stock_picking_ids)/2:])

# for rec in stock_picking_ids:
#     model_stock_picking.unlink(rec)

def chunks(var_list, chunk_size):
    for i in range(0, len(var_list), chunk_size):
        yield var_list[i:i+chunk_size]


chunck_size = 10
i = 1
stock_picking_chunks = list(chunks(stock_picking_ids, chunck_size))
run_count = int(math.ceil(len(stock_picking_ids) / chunck_size) + 1)
for chunk in stock_picking_chunks:
    print 'Process chunk %s of %s' % (i, run_count)
    model_stock_picking.unlink(chunk)
    i += 1

# i = 1
# stock_picking_chunks = list(chunks(stock_picking_ids, 100))
# for chunk in stock_picking_chunks:
#     print 'Process chunk %s of %s' % (i, len(stock_picking_ids))
#     model_stock_picking.unlink(chunk)
#     i += 1
