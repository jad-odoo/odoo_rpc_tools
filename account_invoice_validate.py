# -*- coding: utf-8 -*-
import sys

from odoo_csv_tools.lib import conf_lib
from odoo_csv_tools.lib.internal.rpc_thread import RpcThread

from files import config_file

connection = conf_lib.get_server_connection(config_file)
model_account_invoice = connection.get_model("account.invoice")

recs = model_account_invoice.search([('state', '=', 'draft')])

print 'Invoices to validate: %s' % len(recs)
model_account_invoice.action_invoice_open(recs)

