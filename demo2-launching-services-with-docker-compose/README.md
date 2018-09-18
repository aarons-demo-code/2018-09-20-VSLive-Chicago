# Demo 2 - Launching Services Locally with Docker Compose

This demo shows how to use [Docker Compose](https://docs.docker.com/compose/)
to launch all the external services (i.e. databases) that your app needs,
so that you can test everything locally.

The goal is to make it as easy as possible to run an environment locally
that looks as much like production as possible. Using these tools, we abstract
away the entire production environment, while still being able to test our app
locally.

The example here contains a 
[Docker compose file](https://docs.docker.com/compose/compose-file/) that 
launches and configures [MongoDB](https://www.mongodb.com/), 
[Redis](https://redis.io/) and 
[Minio](https://minio.io/) automatically, with a single command.

This would be a great environment to locally test an application that uses 
a database, a cache and a cloud object storage system, for example.

# Launch The Services

To launch all these services, run:

```console
docker-compose -p vslive up -d all
```

All 3 services were launched in the background and will be starting up.
See them with:

```console
docker ps
```

When you're done, run the following to tear everything down:

```console
docker-compose -p vslive down
```
