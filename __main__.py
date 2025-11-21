import pulumi
from pulumi import Config
import pulumi_digitalocean as do

from modules.network.vpc import create_vpc
from modules.security.firewall import create_firewall

env = pulumi.get_stack()

cfg = Config("pulumi-base-infra-do")
region = cfg.require("region")

do_cfg = Config("digitalocean")
token = do_cfg.require("token")

provider = do.Provider("do-provider", token=token)

vpc = create_vpc(env, region, provider)

pulumi.export("vpc_id", vpc.id)
