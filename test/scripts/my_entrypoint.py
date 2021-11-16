#!/usr/bin/python3
# *_* coding: utf-8 *_*

import os

locust_entry_path = '/locust-cluster/user/scripts/my_locustfile.py'
os.system('locust -f {}'.format(locust_entry_path))