# -*- coding: utf-8 -*-
import odoolib
from odoo_csv_tools.lib import conf_lib
from prefix import *
from files import *

connection = conf_lib.get_server_connection(config_file)


def view_xml_id(connection, module, name):
    data_model = connection.get_model('ir.model.data')
    data_ids = data_model.search([('module', '=', module), ('name', '=', name)])
    records = data_model.read(data_ids, ['model', 'res_id'])
    if not len(records):
        print 'Record not found'
    else:
        record = records[0]
        print 'Model: %s Id: %s' % (record['model'], record['res_id'])

view_xml_id(connection, HELPDESK_TICKET_PREFIX, '132496')



