import boto3
_secrets_ = ('AKIA5R2GKQRMQ7ROQVXZ', '3KD0qDhdtpcPna5ETnkg7DKtY5TneAxoV3Iskd81')
session = boto3.session.Session(aws_access_key_id=_secrets_[0],
                                aws_secret_access_key=_secrets_[1],
                                aws_session_token=None,
                                region_name = 'us-west-2')
s3_client = session.client('s3', region_name='us-west-2', api_version='2006-03-01')