# Description
Vpc setup with 3 private and 3 public subnets in 3 different regions
# Setup
brew install pulumi/tap/pulumi
mkdir foldername
cd foldername
export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID> 
export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
pip3 install pulumi-awsx
Pulumi new aws-python
Pulumi up
