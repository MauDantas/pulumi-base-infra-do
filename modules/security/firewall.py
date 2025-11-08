import pulumi_digitalocean as do

def create_firewall(env: str, vpc: do.Vpc):
    """
    Creates a basic DigitalOcean Firewall attached to the given VPC.
    """
    fw = do.Firewall(
        f"{env}-fw",
        inbound_rules=[
            {
                # Allow SSH from a specific IP (replace YOUR_IP with your actual IP)
                "protocol": "tcp",
                "port_range": "22",
                "source_addresses": ["YOUR_IP/32"],
            },
            {
                "protocol": "tcp",
                "port_range": "443",
                "source_addresses": ["0.0.0.0/0"],
            },
        ],
        outbound_rules=[
            {
                "protocol": "tcp",
                "port_range": "all",
                "destination_addresses": ["0.0.0.0/0"],
            },
        ],
        tags=[f"{env}-infra"],
    )
    return fw
