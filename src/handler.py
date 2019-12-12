# -*- coding: utf-8 -*-
"""
The function need to invoked by timer
Substitute this with you own function, and you can use any other language runtime to implements this

Attention:
  Function must return validate json as FunctionFlow task step needed
"""

import logging
import json


def handler(event, context):
    logger = logging.getLogger()
    logger.info('Input: {}'.format(event))

    evt = json.loads(event)

    # this is second level time trigger event all info you can get
    # just like fc time trigger
    trigger_time = evt['triggerTime']
    trigger_name = evt['triggerName']
    payload = evt.get('payload', '{}')

    # todo do something here

    return event
