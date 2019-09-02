# -*- coding: utf-8 -*-

import openerplib
from prefix import *
from files import *
from odoo_csv_tools.lib import conf_lib

"""
Remove account.payment.term.line created by default at the account.payment.term creation.
"""

connection = conf_lib.get_server_connection(config_file)
                                       
connection.check_login()

model_account_payment_term = connection.get_model('account.payment.term')
model_account_payment_term_line = connection.get_model('account.payment.term.line')
model_data = connection.get_model('ir.model.data')

payment_terms_ids_raw = model_data.search_read([('model', '=', 'account.payment.term'), ('module', '=', 'sodaphi_company1_account_payment_term')], ['res_id'])
payment_terms_ids = []
for rec in payment_terms_ids_raw:
    payment_terms_ids.append(rec['res_id'])

payment_term_line_ids = model_account_payment_term_line.search([('payment_id', 'in', payment_terms_ids), ('value', '=', 'balance'), ('days', '=', '0')])

print 'Remove payment term lines: %s' % payment_term_line_ids

model_account_payment_term_line.unlink(payment_term_line_ids)

