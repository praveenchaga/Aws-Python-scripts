import boto3
def lambda_handler(event, context):
    myRDSclient = boto3.client('rds')    
    response1 = myRDSclient.stop_db_instance(
        DBInstanceIdentifier='praveendb'
    )
    print (response1)