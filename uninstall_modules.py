# -*- coding: utf-8 -*-
import sys
import openerplib
from prefix import *
from files import *
from odoo_csv_tools.lib import conf_lib
from odoo_csv_tools.lib.internal.rpc_thread import RpcThread

from files import config_file

connection = conf_lib.get_server_connection(config_file)
                                      
model_module = connection.get_model("ir.module.module")

module_names = ['dataconsult_module_override']

module_ids = model_module.search_read([["name", "in", module_names]])

rpc_thread = RpcThread(4)

for module in module_ids:
    if module["state"] == "installed":
        print 'Uninstalling %s...' % module["name"]
        rpc_thread.spawn_thread(model_module.button_immediate_uninstall, [module["id"]])
    else:
        print 'Module %s is not installed !' % module["name"]
    # print 'Done.'