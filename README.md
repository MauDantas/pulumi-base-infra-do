# Base Infrastructure on Digital Ocean Using Pulumi
Prove of Concept of Continuos Deploy with Pulumi via Digital Ocean. Pulumi.template.yaml file have instructions on how you should set your configuration file.

# If you are new to Pulumi

- **pulumi stack init staging** to initializa staging env. The same you use to control production environment. Or developer if you go 3 ways
- **pulumi preview** to see what is going to be provisioned
- **pulumi up** and you should get your infrastructure set 

## If you are new to poetry Pack Management

- Poetry shell to isolate your environment (Using venv behind the scenes)
- Poetry install to install dependencies 
- The dependencies are listed on project.toml