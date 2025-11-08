import pulumi_digitalocean as do

def create_vpc(env: str, region: str) -> do.Vpc:
    """
    Creates a DigitalOcean VPC.
    """
    vpc = do.Vpc(
        f"{env}-vpc",
        region=region,
        ip_range="10.0.0.0/16",
        description=f"{env} base VPC"
    )
    return vpc
