#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pprint import pprint

import boto3


if __name__ == '__main__':
    client = boto3.client('lambda')
    name = 'invoke-lambda'
    response = client.invoke(
        FunctionName=name,
        InvocationType='RequestResponse',
        LogType='None',
        Payload=bytes(json.dumps([u'走著瞧', u'警政署']))
    )

    pprint(response)

    resp_data = json.loads(response['Payload'].read().decode("utf-8"))
    pprint(resp_data)
