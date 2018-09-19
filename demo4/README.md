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
az group create --name vslive --location eastus
az aks create --resource-group vslive --name vslive --node-count 3 --enable-addons monitoring --generate-ssh-keys
az aks install-cli
az aks get-credentials --resource-group vslive --name vslive
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

After this command completes, you'll see some output that looks like this:

```console
NAME:   vslive2018
LAST DEPLOYED: Wed Sep 19 17:52:23 2018
NAMESPACE: vslive2018
STATUS: DEPLOYED

RESOURCES:
==> v1/Service
NAME        TYPE          CLUSTER-IP    EXTERNAL-IP  PORT(S)       AGE
vslive2018  LoadBalancer  10.0.238.213  <pending>    80:32097/TCP  1s

==> v1beta1/Deployment
NAME        DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
vslive2018  3        3        3           0          1s

==> v1/Pod(related)
NAME                         READY  STATUS             RESTARTS  AGE
vslive2018-566b85d965-4mfv8  0/1    ContainerCreating  0         1s
vslive2018-566b85d965-knjtt  0/1    ContainerCreating  0         1s
vslive2018-566b85d965-qq2bj  0/1    ContainerCreating  0         1s
```

That's the app's topology and its status, all in one!


## Checking the App's Status

Since Kubernetes is always watching (and things fail, etc...), 
your app's status might change any time. 
You can check the current status whenever you want by running:

```console
helm status vslive2018
```

For example, if you wait a few seconds and run that `helm status` command 
again, your new output will include:

```console
==> v1/Pod(related)
NAME                         READY  STATUS   RESTARTS  AGE
vslive2018-566b85d965-4mfv8  1/1    Running  0         2m
vslive2018-566b85d965-knjtt  1/1    Running  0         2m
vslive2018-566b85d965-qq2bj  1/1    Running  0         2m
```

The `STATUS` column was set to `ContainerCreating` before, and now it's set to `Running`. That means that your containers are completely up and running now!

Since there are three rows, there are three _replicas_ (containers) of your app
running. That's super useful for high availability.

Now, if you wait a few _more_ seconds and run `helm status` again, the output
should include:

```console
==> v1/Service
NAME        TYPE          CLUSTER-IP    EXTERNAL-IP   PORT(S)       AGE
vslive2018  LoadBalancer  10.0.238.213  40.121.91.81  80:32097/TCP  2m
```

That `EXTERNAL-IP` is now filled in. Before, it was `<pending>`. The IP there
is _public_! Behind the scenes, Kubernetes went and requested from Azure
a public load balancer. When that operation finished, Azure returned the public
IP and Kubernetes fetched it and showed it to you :smile:.

## Testing the App Out

Now that you have a public IP, your app is running on the public internet.
We're running the app from [demo 1](/demo1). That's the
`aaronsdemoimages/vslivechicago2018:demo1` container that serves a 
`GET /hello/sayHello` endpoint.

In demo 1, we had to access that server on port 9090, but Kubernetes has 
taken care of all that networking for us and is exposing the server on 
the standard HTTP port 80.

So now you can go to the public IP and do a `GET /hello/sayHello` and you 
should see the same output. Here's what it looks like with 
[`curl`](https://curl.haxx.se/docs/manpage.html) on my Macbook with that above
IP address:

```console
curl http://40.121.91.81/hello/sayHello
Hello, VSLive!
```

It worked!

# Cleaning Up

Helm makes it really easy to delete your entire app from Kubernetes. Be careful with this
because there is no undo! It's really useful for testing your app, but 
if you do it in production, you can bring your entire app to a halt
(I've done that before :frown:)

For this demo, we should definitely delete the app and free up resources
in the cluster. Helm makes that easy:

```console
helm delete --purge vslive2018
```

Now the app is gone from Kubernetes, but your Kubernetes cluster is still
running on AKS. You can leave the cluster up and keep playing around,
or you can delete it and free up the Azure resources it was using
(once you do this, Azure won't charge you for those resources anymore either 
:smile:). Do the cleanup with this:

```console
az aks delete --name vslive --resource-group vslive
```

After that completes, everything will be cleaned up.

Hope to see you back here soon!
