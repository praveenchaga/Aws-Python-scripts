####################################################################################################
# Delete all the un-used security groups wich starts with name "launch-wizard" in Aws-infrastructue
# PRAVEEN KUMAR.CH     chagapraveen@gmail.com                         DATE: 24-05-2018
####################################################################################################

import boto3
ec2 = boto3.client('ec2')
client = boto3.client('ec2')
in_use_groups = []
to_delete_groups = []
allgroupnames = []
all_groups = [group['GroupName'] for group in client.describe_security_groups()['SecurityGroups']]
print "all groups %s" % all_groups

delete_candidates = [item for item in all_groups if item not in in_use_groups and item.startswith('launch-wizard-')]
print delete_candidates

for i in delete_candidates:
   print "security %s" % i
   response = ec2.delete_security_group(GroupName="%s" % i)
   print "deleted group %s" % i
