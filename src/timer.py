# -*-coding: utf-8 -*-
"""
This function will be invoked by FC time trigger. it will execute FnF flow according the trigger payload settings
time trigger payload example:
{"flow_name": "YourFlowName", "input": "{\"duration\": 1}"}
"""
import json
import logging

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkfnf.request.v20190315.StartExecutionRequest import StartExecutionRequest

logger = logging.getLogger()


def initialize(context):
    logger.info('Begin initialization ...')

    global fnf_client
    creds = context.credentials
    sts_creds = StsTokenCredential(creds.access_key_id, creds.access_key_secret, creds.security_token)
    fnf_client = AcsClient(credential=sts_creds, region_id=context.region)

    logger.info('End initialization')


def handler(event, context):
    evt = json.loads(event)
    logger.info('Start execution {} '.format(evt))
    
    payload = evt.get('payload', '{}')
    data = json.loads(payload)
    input = data.get('input', '')
    evt.update(payload=input)

    start_execution(data.get('flow_name', ''), data.get('execution_name', ''), json.dumps(evt), context)


def start_execution(flow_name, execution_name, input, context):
    request = StartExecutionRequest()
    request.set_FlowName(flow_name)
    request.set_ExecutionName(execution_name)
    request.set_Input(input)
    request.set_endpoint('{}-internal.fnf.aliyuncs.com'.format(context.region))
    fnf_client.do_action_with_exception(request)
