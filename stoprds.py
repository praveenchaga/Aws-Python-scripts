############################################################################################################################
#   To Stop specific RDS_ Instance every day @ 23:30 AM IST Automatically in Aws using server less computing (Aws-Lambda)
#   Create IAM role with RDS-full access.
#   Create Lambda function
#   Create cloudwatch event>>Rule using then Cron expression 0 18 ? * MON-FRI * 
#	Mentiond-DB-Instance will be stopped at 18:00 GMT that is 23:30 IST. Weekly five days that is MON-FRI
#  
#   PRAVEEN KUMAR.CH                     chagapraveen@gmail.com                                       Date: 05-06-2018
############################################################################################################################

import boto3
def lambda_handler(event, context):
    RDS = boto3.client('rds')    
    response = RDS.stop_db_instance(
        DBInstanceIdentifier='praveendb'
    )
    print (response)
