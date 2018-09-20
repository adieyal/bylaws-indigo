# bylaws-indigo
Indigo for openbylaws.org.za

# Production deployment

Deployment via dokku.

Indigo-bylaws depends on some private GitHub repos. You need to install some dokku plugins to enable this.

1. Install [dokku-hostkeys-plugin](https://github.com/cedricziel/dokku-hostkeys-plugin) and run `dokku hostkeys:shared:autoadd github.com` so that dokku trusts github.com as a server
2. Install [dokku-deployment-keys](https://github.com/cedricziel/dokku-deployment-keys) and run `dokku deploymentkeys:shared` to get the public portion of the deployment key that dokku will use when cloning private GitHub repos.
3. In the GitHub repo, create a deployment key and copy in the public key from step 2.
