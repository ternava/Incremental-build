
# Running Dockerfile

-------------
(comment: the docker image needs to be in the Docker Hub)

Build an image: `sudo docker build -t="xheva/imagex264" .`
Run a container from it: `docker run --name containerx264 -p 8888:8888 -it xheva/imagex264`

To access the notebook, with all the data, open in the browser the given link after running the container.

Restart the existing container: `docker start -i containerx264`

Delete all containers: `docker rm -f $(docker ps -a -q)`
Delete all images: `docker rmi -f $(docker images -a -q)`