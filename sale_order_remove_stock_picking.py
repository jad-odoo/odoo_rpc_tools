# -*- coding: utf-8 -*-
import sys
from odoo_csv_tools.lib import conf_lib
from odoo_csv_tools.lib.internal.rpc_thread import RpcThread
from files import *
from prefix import *

connection = conf_lib.get_server_connection(config_file)
model_data = connection.get_model('ir.model.data')
model_sale_order = connection.get_model('sale.order')
model_stock_picking = connection.get_model('stock.picking')

data_recs = model_data.search_read([('module', '=', SALE_ORDER_PREFIX), ('model', '=', 'sale.order')], ['res_id'])

so_ids = []
for rec in data_recs:
    so_ids.append(rec['res_id'])

stock_picking_ids = model_stock_picking.search([('sale_id', 'in', so_ids)])

print 'Stock picking to remove: %s' % len(stock_picking_ids)
print stock_picking_ids
model_stock_picking.unlink(stock_picking_ids)
