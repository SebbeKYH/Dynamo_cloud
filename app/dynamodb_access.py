import os
import boto3


def get_resource():
    return boto3.resource('dynamodb',
                          aws_access_key_id=os.environ['AWS_KEY'],
                          aws_secret_access_key=os.environ['AWS_SECRET_KEY'],
                          region_name='eu-north-1')

def get_all_readings():
    client = get_resource()
    table = client.Table('heart_rate_gear_box')
    response = table.scan()
    return response['Items']