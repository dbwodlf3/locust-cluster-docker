#!/usr/bin/python3
# *_* coding: utf-8 *_*

import os
import common

locust_entry_path = os.path.join(common.scriptDir, 'locustfile.py')

os.system('locust -f {} --worker --master-host=locust-cluster-master'.format(locust_entry_path))