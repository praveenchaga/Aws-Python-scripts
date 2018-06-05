import boto3
def lambda_handler(event, context):
    RDS = boto3.client('rds')    
    response = RDS.start_db_instance(
        DBInstanceIdentifier='praveendb'
    )
    print (response)