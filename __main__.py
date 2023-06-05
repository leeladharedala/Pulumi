import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("custom")

pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)