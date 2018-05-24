########################################################################################################################
#   To Start specific Ec2_ Instance every day @ 5:00 AM Automatically in Aws using server less computing (Aws-Lambda)
#   Create IAM role with ec2full access.
#   Create Lambda function
#   Create cloudwatdh event using then Cron expression 0 5 * * ? *
#   Which will show you the next 10 trigger Dates as per below.
#   Fri, 25 May 2018 05:00:00 GMT
#   Sat, 26 May 2018 05:00:00 GMT
#   Sun, 27 May 2018 05:00:00 GMT
#   Mon, 28 May 2018 05:00:00 GMT
#   Tue, 29 May 2018 05:00:00 GMT
#   Wed, 30 May 2018 05:00:00 GMT
#   Thu, 31 May 2018 05:00:00 GMT
#   Fri, 01 Jun 2018 05:00:00 GMT
#   Sat, 02 Jun 2018 05:00:00 GMT
#   Sun, 03 Jun 2018 05:00:00 GMT
#   PRAVEEN KUMAR.CH                     chagapraveen@gmail.com                                       Date: 24-05-2018
########################################################################################################################
#Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2
import boto3
# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g., '	eu-west-1'
region = 'Please enter the region'
# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = ['Please enter the instance ID']
#At the time you create a Lambda function, you specify a handler, which is a function in your code, that AWS Lambda can invoke when the service executes your code. Use the following general syntax structure when creating a handler function in Python.
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.start_instances(InstanceIds=instances)
    print 'Instance has been started : ' + str(instances)
