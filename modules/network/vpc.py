import pulumi
from pulumi import Config
import pulumi_digitalocean as do


def create_vpc(env: str, region: str, provider: do.Provider) -> do.Vpc:
    cfg = Config("vpc")
    ip_range = cfg.require("ip_range")

    return do.Vpc(
        f"{env}-vpc",
        region=region,
        ip_range=ip_range,
        description=f"{env} base VPC",
        opts=pulumi.ResourceOptions(provider=provider)
    )
