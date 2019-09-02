# -*- coding: utf-8 -*-
import sys

from odoo_csv_tools.lib import conf_lib
from odoo_csv_tools.lib.internal.rpc_thread import RpcThread

from files import config_file

connection = conf_lib.get_server_connection(config_file)
model_sale_order = connection.get_model("sale.order")

recs = model_sale_order.search([('state', '=', 'draft')])

print 'Sale orders to validate: %s' % len(recs)
model_sale_order.action_confirm(recs)




# inventory = connection.get_model("stock.inventory")

# inventoryadjustments = inventory.search_read([('state', '=', 'confirm')])
# if len(inventoryadjustments) > 0:
#     sys.stderr.write("There are still {} Inventory Adjustments that haven't been validated yet.".format(len(inventoryadjustments)))

# rpc_thread = RpcThread(4)

# def confirm_sale_order(order):
#     try:
#         global todo
#         todo = todo - 1
#         sale_order.action_confirm(order["id"])
#         print("{} Number of sales orders left".format(todo))
#     except Exception as e:
#         sys.stderr.write("Sale order with id {} and name {} received the following error: {}\n\n\n".format(order["id"], order["name"], e))

# #Wilsons First Threaded
# sys.stderr.write("Wilsons First Threaded\n-------------------------\n\n")
# print("Wilsons First Threaded")
# saleorders = sale_order.search_read([('state', '=', 'draft'), ('company_id', '=', 1)])
# todo = len(saleorders)
# for order in saleorders:
#     rpc_thread.spawn_thread(confirm_sale_order, [order])
# rpc_thread.wait()

# #Wilsons First One by one
# sys.stderr.write("Wilsons First One by one\n-------------------------\n\n")
# print("Wilsons First One by one")
# saleorders = sale_order.search_read([('state', '=', 'draft'), ('company_id', '=', 1)])
# todo = len(saleorders)
# for order in saleorders:
#     confirm_sale_order(order)

# #Generation Second Threaded
# sys.stderr.write("Generation Second Threaded\n-------------------------\n\n")
# print("Generation Second Threaded")
# saleorders = sale_order.search_read([('state', '=', 'draft'), ('company_id', '=', 3)])
# todo = len(saleorders)
# for order in saleorders:
#     rpc_thread.spawn_thread(confirm_sale_order, [order])
# rpc_thread.wait()

# #Generation Second One by one
# sys.stderr.write("Generation Second One by one\n-------------------------\n\n")
# print("Generation Second One by one")
# saleorders = sale_order.search_read([('state', '=', 'draft'), ('company_id', '=', 3)])
# todo = len(saleorders)
# for order in saleorders:
#     confirm_sale_order(order)

