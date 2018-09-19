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
ports to expose, how to route traffic, and more. We can use the `helm` CLI
to deploy a new release or our app to Kubernetes, do upgrades, rollbacks and 
more!

