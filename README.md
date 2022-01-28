### Availability of artefacts:

* __The five open-source software systems used in our experiments__
  
  | Subject  	| Repository                                      |  Commit/Tag ID  	                                                                        | Date  	          |
  |---	      |---	                                            |---                                                                                        |---	              |
  | x264      | https://github.com/mirror/x264                  |  [ae03d92](https://github.com/mirror/x264/tree/ae03d92b52bb7581df2e75d571989cb1ecd19cbd) 	| June 13, 2021 	  |
  | sqlite    | https://github.com/sqlite/sqlite                |  [version-3.35.4](https://github.com/ternava/sqlite/releases/tag/version-3.35.4) 	        | April 02, 2021	  |
  | xz        | https://github.com/xz-mirror/xz                 |  [e7da44d](https://github.com/xz-mirror/xz/tree/e7da44d5151e21f153925781ad29334ae0786101) | February 13, 2021	|
  | curl      | https://github.com/curl/curl                    |  [curl-7_78_0](https://github.com/curl/curl/releases/tag/curl-7_78_0) 	                  | July 21, 2021    	|
  | xterm     | https://github.com/ThomasDickey/xterm-snapshots |  [xterm-368](https://github.com/ThomasDickey/xterm-snapshots/releases/tag/xterm-368)      | June 08, 2021    	|

---

### Artefact description

* __How is delivered__

  Our used data, scripts, and obtained results are publicly available in these following places: 
  - In this repository under the releases ******* 
  - In a stable release in Zenodo at https://doi.org/10.5281/zenodo.5907901.
  - The raw resulting data are in 


* __Project Structure__

  In addition to the `main` branch, this project has 5 other relevant branches: 
  [inc-build-x264](https://github.com/ternava/Incremental-build/tree/inc-build-x264), 
  [inc-build-sqlite](https://github.com/ternava/Incremental-build/tree/inc-build-sqlite),
  [inc-build-xz](https://github.com/ternava/Incremental-build/tree/inc-build-xz),
  [inc-build-curl](https://github.com/ternava/Incremental-build/tree/inc-build-curl), and
  [inc-build-xterm](https://github.com/ternava/Incremental-build/tree/inc-build-xterm).
  Thus, all generated artefacts and obtained data are recorded in a specific branch for each subject system. 

 * __Branch Structure__
  
   Each branch has this following folder structure: 
  
    ```yaml
    inc-build-[SystemName] (branch)
    │
    └─── artifacts                                           
    │   │   fm-[SystemName]-ib.png
    └─── configurations
    │   └─── sample-03
    │   └─── sample-04 
    └─── data
    │   └─── rez_sample_03ALL
    │   └─── rez_sample_03I
    │   └─── rez_sample_03II
    │   └─── rez_sample_04ALL
    │   └─── rez_sample_04I
    │   └─── rez_sample_04II
    └─── notebooks
    │   └─── rez_sample_03I
    │       └─── figures
    │   └─── rez_sample_04I
    │       └─── figures
    └─── scripts
    │   Dockerfile 
    │   README.md
    ```
  
    * _`artifacts`_ folder contains the configuration options model of the system. This model has all compile-time options of the system, including their dependencies, that we used in our experiments. These options are shown by using `$ ./configuration --help` in a system. The model is build using [FeatureIDE](https://featureide.github.io/). This model and FeatureIDE framework is further used to generate the two batches with configurations, given in the folder `configurations`.

    * _`configurations`_ folder contains two subfolders, `sample-03` and `sample-04`. These subfolders contain the Batch 1 (B1) and Batch 2 (B2) with 20 configurations each for the system. These are the used configurations in our experiments. 
    
    * _`data`_ folder contains the generated data after running the scripts given in the `scripts` folder.

    * _`notebooks`_ folder contains the analysed data and generated tables and figures given in the paper, based on the generated data in `data`folder

    * _`scripts`_ folder contains the used scripts to run our experiments. These scripts are also run by using the `Dockerfile`.

    * _`Dockerfile`_ folder contains the instructions to automate the build of experiments and the generated data are made available in a Jupyter notebook.


### REPRODUCE

  To reproduce our work, you need to follow these steps:
  1. Obtain the used scripts to run the experiments
  2. Run those scripts
  3. Process the obtained results



### Batches of configurations

In each system we have used two batched of configurations. They are available within the folder `configurations` under the names `sample-03`(batch 1) and `sample-04` (batch 2).
These configurations remain unchanged in order to reproduce our study. 


### Hardware dependencies

The underlying hardware in the used workstation may impact the obtained time measurements in our experiment.
Our used hardware model is _Dell Inc. Latitude 7410_, with a _memory 15.3 GiB_, _processor Intel® Core™ i7-10610U CPU @ 1.80GHz x 8_. 
Still, any similar architecture (we have already tried in another similar architecture) should give comparable results.


### Required resources

Approximate time taken and used resoures in our used workstation were as in the following table. These resources are needed for the analysis of once batch of configuration of system. If you run 2 batches and repeat them 2 times, then you will need 4 times more of these resources.

  | Resources    	| x264      | sqlite      | xz        | curl      | xterm       |
  |---	          |---	      |---          |---	      |---        |---          |
  | Time          | ~4h       |  ~2h  	    | ~2h       | ~6h       |  ~3h        |
  | Space         | 3.34GB    |  4.41GB     | 2.62GB 	  | 5.65GB    |  2.47GB     |

### Software prerequisites

-  Check if you have __docker__ installed by typing `sudo docker --version` in a terminal. If not, then you need to [install it](https://docs.docker.com/get-docker/).
-  If docker is installed, you may need to check whether the docker engine is running by typing `sudo systemctl status docker` in a terminal. If it's not running then start it by typing `sudo systemctl start docker`. 

- Check if you have __git__ installed by typing `git --version` in a terminal. If not, then (optionally) you need to [install it](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

### Running our experiments

- **Step 1:** Open e terminal (you can use the terminal within an IDE, e.g., within Visual Studio Code). Somewhere in your directory, create a local copy of this project, e.g., by typing `git clone https://github.com/ternava/Incremental-build.git` in a terminal. 
- **Step 2:** By being in the path of this project, enter in the cloned project by typing `cd Incremental-build`. 
- **Step 3:** If you type `git branch`, it will show you that you are in the `main` branch. To run experiments with a specific software project, you need to switch to a specific branch (see the __Project Structure__). For instance, to run experiments with _x264_ software system you first need to switch to its branch. To do that, in the terminal you type `git checkout inc-build-x264`. In the following is shown how to run experiments with _x264_, then the same process can be applied for the rest.
- **Step 4:** By being in the `inc-build-x264` branch, build an image from the _Dockerfile_ by typing `sudo docker build -t="imagex264" .` (don't forget the dot at the end, but you are free to change the `imagex264` image name).
- **Step 5:** Depending from the analysed project, step 4 will take between 2-4 hours to be finished. We thught to provide an example with few configurations that will run quicker, but using few data in the next steps of our experiment make impossible to compare with the original results.
- **Step 6:** Now you should have the results.
    - **Step 6.1:** In case that you want to see the clean and incremental build configurations of _x264_, you need to run a container from the first before the last image and to enter. First, type `docker images -a`. It will show all built docker images. Take the image ID from the first before the last one, which may look like ~~`60e74b672f3f`~~, and type `docker container run -it` ~~`60e74b672f3f`~~. Then, by typing `git branch -a` it will show all clean and incremental build configurations that are saved in separate branches, just as they are described in our approach in Figure 4 in the original paper. To exit from the container type `Ctrl+Z` and then `Ctrl+D` twice.
    - **Step 6.2:** The clean and incremental build time and executable binary sizes for each configuration are avilable within the `/src/data/` folder in files `buildtime_dc2.csv` (clean build data) and `buildtime_di1.csv` (incremental build data) files. If you want to copy these data from container to the host, you should be outside the container and then type `docker cp <containerId>:/file/path/within/container /host/path/target`. But, you can access these data by using our provided Jupyter notebooks. Hence, you can skip this step.
- **Step 7:** Run a container from the build image by `docker run --name containerx264 -p 8888:8888 -it imagex264`. (Note: if you have changed the `imagex264` name in **Step 4**, then you should change it here too.)
- **Step 8:** To access the notebook, with all the data, open in the browser the given link in the terminal after running the container. ~~For example, http://127.0.0.1:8888/?token=7e13ccabbc597bce788a9ce8114ec4b1ab5e3ad06de75082 (this one will not open on your side).~~ It will open a new tab on your web browser. 
- **Step 9:** You will see only the *notebooks* directory structure similar to the one provided here in the **Branch Structure** and within each branch in this project.
- **Step 10:** This directory contains 5 notebooks. Click the first one and it will open a new tab. In the menubar search for the _Kernel -> Restart and run all_ and click it. It will refresh the notebook with your data from the run experiment. You need to do this for each notebook in order (the order is mandatory).
- **Step 11:** You can compare your obtained data with those that we have provided in Table 2 in the original conference paper. These data are further processed, analysed, and showed in Figures 6 - 8 and Tables 3 - 4. 
- **Step 12:** To stop the container, type exit in the terminal or quit the notebooks.

This was just an illustrative example. But, the exact same steps should be followed to build all configurations in batch 1 or barch 2 of a given system. 

- **Step 13:** In that case, check if you are in the path of cloned project, that is, within the `Incremental-build` folder (as shown in **Step 2**).
- **Step 14:** As mentioned in **Step 3**, you can switch to a specific branch, depending with which project you want to experiment.
- **Step 15:** In whichever 5 project branches that you are, you can decide to experiment with the Batch 1 or Batch 2 of its configurations. To switch between batches, open the file `/scripts/options.py` with an editor or type `nano -l scripts/options.py` in the terminal. Then, as explained in the comment in lines 14-16, you can switch between batches by changing the line 18. 
- **Step 16:**  Repeat **Step 4 - Step 12**. 







### How to obtain the artifact package

### How to reproduce the results presented in the paper

- (for the results in the paper) First switch to the right branch, then run the Dockerfile. (what are the storage requirements?)



  

  
In order to replicate our study, the condiguration set within a system can be changed or the subject systems can be changed. 



