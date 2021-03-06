# Demo 1 - Building and Pushing a Docker Image

This demo shows how to build a docker image from an app, and push it
to [Docker Hub](https://hub.docker/com) (a popular Docker image registry).

# About the App

The app we're working with is a tiny HTTP server, written using the 
[Ballerina Programming Language](https://ballerina.io/).

I chose this language on purpose because it's obscure (right now) but I love it.
You might not have heard of it or used it, but one of the big benefits of 
Docker is that you don't need to use the Ballerina toolchain at all if you 
don't want to, even to do local develompent.

In fact, if someone else built the app and the Docker image for it, 
you don't need to know about the technology at all in order to run it :smile:!

The rest of this documentation shows how to build, run, pull, and push the app.

# To Build the Image

Run this to build the image:

```console
docker build -t aaronsdemoimages/vslivechicago2018:demo1 .
```

# To Push the Image

After you've built the image, run the following to push it up to Docker Hub.

```console
docker push aaronsdemoimages/vslivechicago2018:demo1
```

You'll need to have write credentials to do the push.

# To Pull the App

The image for this app is pushed to [Docker Hub](https://hub.docker.com) 
as 
[`aaronsdemoimages/vslivechicago2018:demo1`](https://hub.docker.com/r/aaronsdemoimages/vslivechicago2018/).

To pull it down to your machine, run:

```console
docker pull aaronsdemoimages/vslivechicago2018:demo1
```

# To Run the App

After you've built the image, you'll probably want to run it. Same goes for 
after it's pushed (hint: it's already pushed to 
[`aaronsdemoimages/vslivechicago2018:demo1`](https://hub.docker.com/r/aaronsdemoimages/vslivechicago2018/) 
on Docker Hub)

Make sure you've built or pulled the image, and then do this:

```console
docker run -p 9090:9090 -d --name vslive --rm aaronsdemoimages/vslivechicago2018:demo1
```

This will run it in the background. To get logs, run:

```console
docker logs -f vslive
```

This command will "follow" the logs, so the command won't exit unless you 
"ctrl+c" it. Once you have the logs showing, you'll see a line that indicates
the server is listening:

```console
ballerina: started HTTP/WS endpoint 0.0.0.0:9090
```

Then, open a new terminal window or browser and access `http://localhost:9090/hello/sayHello` to see the app running!

To shut it down, run:

```console
docker rm -f vslive
```
