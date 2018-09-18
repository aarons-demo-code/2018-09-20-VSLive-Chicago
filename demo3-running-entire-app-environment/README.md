# Demo 2 - Running an Entire App Environment Locally

This demo shows how to use [Docker Compose](https://docs.docker.com/compose/)
to launch all the external services (i.e. databases) that your app needs, 
along with the app, all with one command.

After you run that one command, you'll have your app available and running 
so that you can test everything in an environment that's very similar to 
production.

The example here contains a 
[Docker compose file](https://docs.docker.com/compose/compose-file/) that 
launches and configures [MongoDB](https://www.mongodb.com/), 
[Redis](https://redis.io/), [Minio](https://minio.io/), and the app
automatically, with a single command.

# Launch The Services

To launch all these services, run:

```console
docker-compose -p vslive3 up --build all
```

All 3 services and the app were launched in the background and will be 
starting up. See them with:

```console
docker ps
```

When you're done, run the following to tear everything down:

```console
docker-compose -p vslive3 down
```
