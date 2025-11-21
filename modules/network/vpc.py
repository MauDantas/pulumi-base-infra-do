import pulumi
import pulumi_digitalocean as do

def create_vpc(env: str, region: str, provider: do.Provider) -> do.Vpc:
    return do.Vpc(
        f"{env}-vpc",
        region=region,
        ip_range="10.0.99.0/16",
        description=f"{env} base VPC",
        opts=pulumi.ResourceOptions(provider=provider)
    )
