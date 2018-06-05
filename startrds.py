############################################################################################################################
#   To Start specific RDS_ Instance every day @ 11:30 AM IST Automatically in Aws using server less computing (Aws-Lambda)
#   Create IAM role with RDS-full access.
#   Create Lambda function
#   Create cloudwatdh event using then Cron expression 0 6 ? * MON-FRI *
#	Mentioned DB-Instance will be Start at 06:00 GMT that is 11:30 IST. Weekly five days that is MON-FRI
#  
#   PRAVEEN KUMAR.CH                     chagapraveen@gmail.com                                       Date: 05-06-2018
############################################################################################################################
import boto3
def lambda_handler(event, context):
    RDS = boto3.client('rds')    
    response = RDS.start_db_instance(
        DBInstanceIdentifier='praveendb'
    )
    print (response)
