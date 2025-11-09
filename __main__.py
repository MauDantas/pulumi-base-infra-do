import pulumi
from pulumi import Config
from modules.network.vpc import create_vpc
from modules.security.firewall import create_firewall

# Basic config values
env = pulumi.get_stack()
config = Config()
region = config.require("region")

# Create VPC
vpc = create_vpc(env, region)

# Create firewall (commented in case you need a pre-existing firewall, not really relevant right now)
# firewall = create_firewall(env, vpc)

# Export identifiers
pulumi.export("vpc_id", vpc.id)
