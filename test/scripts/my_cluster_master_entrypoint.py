#!/usr/bin/python3
# *_* coding: utf-8 *_*

import os

entry_path = '/locust-cluster/user/scripts/my_locustfile.py'
web_port = 9000

os.system('locust -f {} --master --web-port {}'.format(
    entry_path, web_port)
)