import pulumi
from modules.network.vpc import create_vpc
from modules.network.subnet import create_subnets
from modules.security.firewall import create_firewall

# Basic config values
env = pulumi.get_stack()
region = "nyc3"

# Create VPC
vpc = create_vpc(env, region)

# Create subnets (optional, DO VPC covers the region)
subnets = create_subnets(vpc, env)

# Create firewall
firewall = create_firewall(env, vpc)

# Export identifiers
pulumi.export("vpc_id", vpc.id)
