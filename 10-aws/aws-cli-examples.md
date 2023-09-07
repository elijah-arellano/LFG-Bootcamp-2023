aws ec2 describe-images

aws ec2 describe-instance-types

aws ec2 create-key-pair --key-name MyDemoKeyPair

aws ec2 create-security-group --group-name MyDemoSecurityGroup --description "My Demo security group"

aws ec2 authorize-security-group-ingress --group-name MyDemoSecurityGroup --protocol tcp --port 22 --cidr 0.0.0.0/0

aws ec2 run-instances --image-id ami-002068ed284fb165b --count 1 --instance-type t2.micro --key-name MyDemoKeyPair --security-group-ids  sg-07b74523797263314

aws ec2 describe-instances

aws ec2 terminate-instances --instance-ids i-06c1283261aeb19b7


## create auto scaling group

aws autoscaling create-auto-scaling-group --auto-scaling-group-name ASG2 --launch-template "LaunchTemplateName=MyEC2WebApp" --min-size 1 --max-size 3 --desired-capacity 2 --availability-zones "us-east-1a" "us-east-1b" --vpc-zone-identifier "subnet-02a94e365a7db9848, subnet-00fcec5c9dcd1077d"

## create load balancer, create listener, and attach to TG1 to ASG2

aws elbv2 create-load-balancer --name ALB2 --subnets subnet-02a94e365a7db9848 subnet-00fcec5c9dcd1077d --security-groups sg-018ef94c41893157d

aws elbv2 create-listener --load-balancer-arn arn:aws:elasticloadbalancing:us-east-1:821711655051:loadbalancer/app/ALB2/c3276fdb62a22113 --protocol HTTP --port 80 --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-east-1:821711655051:targetgroup/TG1/e47504d36c5b8a7f

aws autoscaling attach-load-balancer-target-groups --auto-scaling-group-name ASG2 --target-group-arns arn:aws:elasticloadbalancing:us-east-1:821711655051:targetgroup/TG1/e47504d36c5b8a7f

## delete ASG2 and ALB2

aws elbv2 delete-load-balancer --load-balancer-arn arn:aws:elasticloadbalancing:us-east-1:821711655051:loadbalancer/app/ALB2/c3276fdb62a22113

aws autoscaling delete-auto-scaling-group --auto-scaling-group-name ASG2 --force-delete

## Filtering the output ##
aws ec2 describe-volumes --region="ap-south-1" --query 'Volumes[].[Attachments,State,VolumeId]'