# -*- coding: utf-8 -*-
import openerplib
from prefix import *
from files import *
from odoo_csv_tools.lib import conf_lib

connection = conf_lib.get_server_connection(config_file)

model_lang = connection.get_model("base.language.install")

for key in res_lang_map.keys():
    lang = res_lang_map[key]
    print 'Install language %s' % lang
    res = model_lang.create({'lang': lang})
    model_lang.lang_install(res)
