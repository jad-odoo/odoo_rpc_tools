# -*- coding: utf-8 -*-
import sys

from odoo_csv_tools.lib import conf_lib
from odoo_csv_tools.lib.internal.rpc_thread import RpcThread

from files import config_file

connection = conf_lib.get_server_connection(config_file)
model_purchase_order = connection.get_model("purchase.order")

recs = model_purchase_order.search([('state', '=', 'draft')])

print 'Purchase orders to validate: %s' % len(recs)
model_purchase_order.button_confirm(recs)

