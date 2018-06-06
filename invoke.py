#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pprint import pprint

import boto3


if __name__ == '__main__':
    client = boto3.client('lambda')
    name = 'awscodestar-invoke-lambda-lambda-HelloWorld-5WPI2EY6ZR6A'
    response = client.invoke(
        FunctionName=name,
        InvocationType='RequestResponse',
        LogType='None',
    )

    pprint(response)
    pprint(json.loads(response['Payload'].read().decode("utf-8")))