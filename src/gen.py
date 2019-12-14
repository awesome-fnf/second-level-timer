# -*- coding: utf-8 -*-
"""
The function used to generate wait intervals, no need to modify
"""

import logging
import json
from datetime import datetime

RFC = '%Y-%m-%dT%H:%M:%SZ'


def handler(event, context):
    logger = logging.getLogger()
    logger.info('Input: {}'.format(event))

    evt = json.loads(event)
    trigger_time = evt['triggerTime']
    duration = int(evt.get('duration', '1'))
    trigger_timestamp = datetime.strptime(trigger_time, RFC).timestamp()

    intervals = []
    wait = 0
    while wait < 60:
        intervals.append(datetime.fromtimestamp(trigger_timestamp + wait).strftime(RFC))
        wait += duration

    data = {
        'waits': intervals,
    }
    return json.dumps(data)
