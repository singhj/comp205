import boto3
session = boto3.session.Session(aws_access_key_id=_secrets_[0],
                                aws_secret_access_key=_secrets_[1],
                                aws_session_token=None,
                                region_name = 'us-west-2')
s3_client = session.client('s3', region_name='us-west-2', api_version='2006-03-01')
