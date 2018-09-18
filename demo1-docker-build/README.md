# Demo 1 - Building and Pushing a Docker Image

This demo shows how to build a docker image from an app, and push it
to [Docker Hub](https://hub.docker/com) (a popular Docker image registry).

The app is written using the 
[Ballerina Programming Language](https://ballerina.io/), but you don't 
need to know that language or even have the Ballerina toolchain installed
to run the app. See below on how to build, push and run the app.

# To Build the App

Run this to build the app:

```console
docker build -t aaronsdemoimages/vslivechicago2018:demo1 .
```

# To Pull the App

The image for this app is pushed to [Docker Hub](https://hub.docker.com) 
as [`aaronsdemoimages/vslivechicago2018:demo1`](https://hub.docker.com).

To pull it down to your machine, run:

```console
docker pull aaronsdemoimages/vslivechicago2018:demo1
```

# To Push the App

After you've built the app, run the following to push it up to Docker Hub.

```console
docker push aaronsdemoimages/vslivechicago2018:demo1
```

You'll need to have write credentials to do the push.

# To Run the App

Make sure you've built or pulled the app, and then do this:

```console
docker run -p 9090:9090 aaronsdemoimages/vslivechicago2018:demo1
```

After it's running, it should have logs that end with:

```console
ballerina: started HTTP/WS endpoint 0.0.0.0:9090
```

Then, open a new terminal window or browser and access `http://localhost:9090/hello/sayHello`
