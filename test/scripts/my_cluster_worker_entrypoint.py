#!/usr/bin/python3
# *_* coding: utf-8 *_*

import os

entry_path = '/locust-cluster/user/scripts/my_locustfile.py'

os.system('locust -f {} --worker --master-host=locust-cluster-master'.format(entry_path))