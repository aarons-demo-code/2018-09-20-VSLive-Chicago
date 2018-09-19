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

# The Application Container

The application container is built from the `Dockerfile` in this directory, and
it's pushed to Docker Hub as `aaronsdemoimages/vslivechicago2018:demo3`. But you
can build it yourself too! To do that, run:

```console
docker build -t aaronsdemoimages/vslivechicago2018:demo3 .
```

You can also use a different image name, too. Just replace 
`aaronsdemoimages/vslivechicago2018:demo3` with your own name. The 
Docker Compose file in here will always use that image though, so if you use the 
`docker-compose` commands below, you'll need to build that image to see changes.

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
