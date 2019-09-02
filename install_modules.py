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
model_module.update_list()

module_names = ['dataconsult_import_base', 'import_metadata', 'dataconsult_module_override']
# module_names = ['dataconsult_import_base', 'dataconsult_module_override']

module_ids = model_module.search_read([["name", "in", module_names]])

rpc_thread = RpcThread(4)

for module in module_ids:
    if module["state"] == "installed":
        # print '%s has already been installed.' % module["name"]
        print 'Upgrading %s...' % module["name"]
        rpc_thread.spawn_thread(model_module.button_immediate_upgrade, [module["id"]])
    else:
        print 'Installing %s...' % module["name"]
        rpc_thread.spawn_thread(model_module.button_immediate_install, [module["id"]])
    # print 'Done.'