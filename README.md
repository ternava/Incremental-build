 
  | Subject  	| Repository                                      |  Commit/Tag ID  	                                                                        | Date  	          |
  |---	      |---	                                            |---                                                                                        |---	              |
  | xz        | https://github.com/xz-mirror/xz                 |  [e7da44d](https://github.com/xz-mirror/xz/tree/e7da44d5151e21f153925781ad29334ae0786101) | February 13, 2021	|

# Running the experiments by using the Dockerfile

(comment: the docker image will be added also in the Docker Hub)
 
- **Step 1:** Check if you have the docker installed by typing `sudo docker --version` in a terminal. If not, then you need to [install it](https://docs.docker.com/get-docker/).
- **Step 2:** If docker is installed, you may need to check whether the docker engine is running by typing `sudo systemctl status docker` in a terminal. If it's not running then start it by typing `sudo status docker start`. 
- **Step 3:** Clone this project, e.g., by `git clone <project git>` and switch to this branch by `git checkout inc-build-xz`.
- **Step 4:** By being in the path of this project, build an image from the Dockerfile by typing `sudo docker build -t="imagexz" .` (don't forget the dot at the end, but you can change the `imagexz` image name).
- **Step 5:** Run a container from the build image by `docker run --name containerxz -p 8888:8888 -it imagexz`.
- **Step 6:** To access the notebook, with all the data, open in the browser the given link after running the container.

Aside notes: 
- Restart the existing container: `docker start -i containerxz`
- Delete all containers: `docker rm -f $(docker ps -a -q)`
- Delete all images: `docker rmi -f $(docker images -a -q)`
