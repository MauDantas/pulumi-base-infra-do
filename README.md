# Base Infrastructure on Digital Ocean Using Pulumi
Prove of Concept of Continuos Deploy with Pulumi via Digital Ocean. Pulumi.template.yaml file have instructions on how you should set your configuration file.

# If you are new to Pulumi

- **pulumi stack init staging** to initializa staging env. The same you use to control production environment. Or developer if you go 3 ways
- **pulumi preview** to see what is going to be provisioned
- **pulumi up** and you should get your infrastructure set 

# To configure your S3 Compatible state with Pulumi

**Ensure you are logged out and offline**
   ```bash
pulumi logout || true
```
**Export credentials**

   ```bash
   export SPACES_ACCESS_KEY_ID=<digital-ocean-s3-key>
   export SPACES_SECRET_ACCESS_KEY=<secret-for-key>
   export DIGITALOCEAN_TOKEN=<your-token>
   export AWS_ACCESS_KEY_ID="$SPACES_ACCESS_KEY_ID"
   export AWS_SECRET_ACCESS_KEY="$SPACES_SECRET_ACCESS_KEY"
   export AWS_REGION=us-east-1
   export AWS_S3_FORCE_PATH_STYLE=true
   export AWS_ENDPOINT_URL_S3=https://s3.example.com
   ```

**Test connection**

   ```bash
   aws s3 ls --endpoint-url $AWS_ENDPOINT_URL_S3
   ```

**Initialize Pulumi with a local backend**
   ```bash
pulumi login file://$HOME/.pulumi
pulumi stack init YOUR_PULUMI_YAML
```

**Sync local Pulumi state to S3**

   ```bash
aws s3 cp Pulumi.YOUR_STACK_NAME.yaml s3://YOUR_BUCKET_NAME/states/
   ```

# If you want to copy my Actions Workflow
```bash
PULUMI_ACCESS_TOKEN= file://$HOME/.pulumi
PULUMI_CONFIG_PASSPHRASE=YOUR_PASSPHRASE
DIGITAL_OCEAN_REGION=YOUR_REGION
DIGITAL_PRIVATE_NETWORK=YOUR_PRIVATE_NETWORK
DIGITAL_OCEAN_TOKEN=YOUR_DIGITAL_OCEAN_ACCESS_TOKEN
SPACES_SECRET_ACCESS_KEY=YOUR_S3_LIKE_ACCESS_KEY
SPACES_ENDPOINT_URL=YOUR_S3_LIKE_SECRET_ACCESS_KEY
AWS_REGION=YOUR_S3_REGION
AWS_EC2_METADATA_DISABLED=true
AWS_S3_FORCE_PATH_STYLE=true
AWS_ENDPOINT_URL_S3=YOUR_S3_LIKE_URL
BUCKET_NAME=YOUR_BUCKET_NAME
```

## If you are new to poetry Pack Management

- Poetry shell to isolate your environment (Using venv behind the scenes)
- Poetry install to install dependencies 
- The dependencies are listed on project.toml