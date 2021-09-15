#!/usr/bin/python3
# *_* coding: utf-8 *_*

import os
import common

locust_entry_path = os.path.join(common.scriptDir, 'locustfile.py')
web_port = 9000

os.system('locust -f {} --master --web-port {}'.format(
    locust_entry_path, web_port)
)