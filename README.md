# Running Dockerfile

(comment: the docker image will be added also in the Docker Hub)

- Build an image: `sudo docker build -t youraccount/image_curl .`
- Run a container from it: `docker run --name container_curl -p 8888:8888 -it youraccount/image_curl`

To access the notebook, with all the data, open in the browser the given link after running the container.

- Restart the existing container: `docker start -i container_curl`
- Create a contained and run an iterative bash shell: `docker run -it youraccount/image_curl`

If needed:

- Delete all containers: `docker rm -f $(docker ps -a -q)`
- Delete all images: `docker rmi -f $(docker images -a -q)`