# Demo 4 - Deploying a Container to Kubernetes

This demo shows how to deploy a container to Kubernetes. We're going to
use 
[Azure Kubernetes Service](https://docs.microsoft.com/en-us/azure/aks/intro-kubernetes) and 
[Helm](https://helm.sh) to take our container we created in [demo 1](/demo1)
and deploy it to our Kubernetes cluster.

# About This Directory

This directory holds a [Helm Chart](https://docs.helm.sh/developing_charts)
that deploys our `aaronsdemoimages/vslivechicago2018:demo1` container
(from [demo 1](/demo1)) to Kubernetes, and exposes it to the internet :smile:.

A Helm chart holds all the details of our app - what container to run, what
ports to expose, how to route traffic, and more. All those details are
written down in Kubernetes manifests, stored in in the 
[templates/](./templates) directory. 

We can use the `helm` CLI to deploy a new release or our app to Kubernetes, 
do upgrades, rollbacks and more!

# Setup

To deploy the container to your own Kubernetes cluster, make sure you have:

- A Kubernetes cluster created and configured
- The `helm` CLI installed
- The Helm server installed (this server is called "Tiller")

Please do these installations in order, and see below for detailed 
instructions.

## Create and Configure your Kubernetes Cluster

I recommend using a managed Kubernetes service to do all of this. If you're
using 
[Azure Kubernetes Service](https://docs.microsoft.com/en-us/azure/aks/intro-kubernetes),
use these commands to set everything up:

```console
az group create --name vslive2018 --location eastus
az aks create --resource-group vslive2018 --name vslive2018Cluster --node-count 3 --enable-addons monitoring --generate-ssh-keys
az aks install-cli
az aks get-credentials --resource-group vslive2018 --name vslive2018Cluster
```

See the 
[AKS Walkthrough](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough)
for more information on creating an AKS cluster and using the `az` commands 
above.

## Install the `helm` CLI

Please see the instructions for installing the Helm client on the
[official Helm documentation page](https://docs.helm.sh/using_helm/#installing-the-helm-client).

## Install the Helm Server

The Helm server, called Tiller, runs inside the Kubernetes cluster and accepts
all the requests to manipulate your app. Please execute the following commands
from inside this directory:

```console
kubectl create -f rbac-config.yaml
helm init --service-account tiller
```

# Deploy the App!

Now that you have your cluster set up and Helm installed, you're ready to 
install your application. You only need to do the setup once, and from
now on, you can launch and manage your application as much as you want. 
Below are some sample commands you can use.

To install your application for the first time, run the following command 
from inside this directory:

```console
helm install --name vslive2018 --namespace vslive2018 ./
```

To uninstall your application after you've installed it, run the following
command from inside this directory:

```console
helm delete --purge vslive2018
```
