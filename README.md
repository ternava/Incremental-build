---
### Table of Content

1. [Artifact description](https://github.com/ternava/Incremental-build/tree/main#1-artifact-description)
    * 1.1. [How is delivered](https://github.com/ternava/Incremental-build#11-how-is-delivered)
    * 1.2. [Hardware dependencies](https://github.com/ternava/Incremental-build#12-hardware-dependencies)
    * 1.3. [Software dependencies](https://github.com/ternava/Incremental-build#13-software-dependencies)
    * 1.4. [Required resources](https://github.com/ternava/Incremental-build#14-required-resources)
   
2. [Project structure](https://github.com/ternava/Incremental-build#2-project-structure)
3. [Branch structure](https://github.com/ternava/Incremental-build#3-branch-structure)
4. [REPRODUCE](https://github.com/ternava/Incremental-build#4-reproduce)
    * 4.1. [Batches of configurations](https://github.com/ternava/Incremental-build#41-batches-of-configurations)
    * 4.2. [Prerequisites](https://github.com/ternava/Incremental-build#42-prerequisites)
    * 4.3. [A QUICK running example](https://github.com/ternava/Incremental-build#43-a-quick-running-example)
    * 4.4. [A COMPLETE reproduction](https://github.com/ternava/Incremental-build#43-a-complete-reproduction)
5. [How to REPLICATE the experiments?](https://github.com/ternava/Incremental-build#5-how-to-replicate-the-experiments)
 


---

### 1. Artifact description

#### 1.1. How is delivered

  Our used data, scripts, and obtained results are publicly available in these following places.
  
  - In this repository under the releases (one release per each branch)
      - [ICSE22-artifact-main-v01](https://github.com/ternava/Incremental-build/releases/tag/ICSE22-artifact-main-v05)
      - [ICSE22-artifact-x264-v01](https://github.com/ternava/Incremental-build/releases/tag/ICSE22-artifact-x264-v01)
      - [ICSE22-artifact-sqlite-v01](https://github.com/ternava/Incremental-build/releases/tag/ICSE22-artifact-sqlite-v01)
      - [ICSE22-artifact-xz-v01](https://github.com/ternava/Incremental-build/releases/tag/ICSE22-artifact-xz-v01)
      - [ICSE22-artifact-curl-v01](https://github.com/ternava/Incremental-build/releases/tag/ICSE22-artifact-curl-v01)
      - [ICSE22-artifact-xterm-v01](https://github.com/ternava/Incremental-build/releases/tag/ICSE22-artifact-xterm-v01)
   
  - **In a stable release in Zenodo at https://doi.org/10.5281/zenodo.5915116.** 

#### 1.2. Hardware dependencies

The underlying hardware in the used workstation may impact the obtained time measurements in our experiment.
Our used hardware model is _Dell Inc. Latitude 7410_, with a _memory 15.3 GiB_, _processor Intel?? Core??? i7-10610U CPU @ 1.80GHz x 8_. 
Still, any similar architecture (we have already tried in another similar architecture) should give comparable results.

#### 1.3. Software dependencies

In our experiments we have used:
   - [Docker](https://docs.docker.com/get-docker/) - to run our experiments (we used version 20.10.12)
   - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - to clone and easily navigate through our project (we used version 2.34.1)
   - [Python](https://www.python.org/downloads/) with [Jupyter](https://jupyter.org/install) and [Pandas](https://pandas.pydata.org/docs/getting_started/install.html) - to process the obtained results (we used Python 3.9.9, Jupyter core 4.7.0, and Pandas 1.2.5)
   - [Graphviz](https://pypi.org/project/graphviz/) - to visualise the graphs for the incremental build order (we used version 0.19.1)

The underlying workstation was Fedora 34, 64-bit, where experiments are run and processed. 
The chosen workstation should not directly impact the obtained results.

#### 1.4. Required resources

Approximate time taken and used resoures in our used workstation were as in the following table. These resources are needed for the analysis of once batch of configuration of system. If you run 2 batches and repeat them 2 times, then you will need 4 times more of these resources.

  | Resources    	| x264      | sqlite      | xz        | curl      | xterm       |
  |---	          |---	      |---          |---	      |---        |---          |
  | Time          | ~4h       |  ~2h  	    | ~2h       | ~6h       |  ~3h        |
  | Space         | 3.34GB    |  4.41GB     | 2.62GB 	  | 5.65GB    |  2.47GB     |
  
  
### 2. Project structure

  - In addition to the `main` branch, this project has 5 other relevant branches: 
    - [inc-build-x264](https://github.com/ternava/Incremental-build/tree/inc-build-x264)
    - [inc-build-sqlite](https://github.com/ternava/Incremental-build/tree/inc-build-sqlite)
    - [inc-build-xz](https://github.com/ternava/Incremental-build/tree/inc-build-xz)
    - [inc-build-curl](https://github.com/ternava/Incremental-build/tree/inc-build-curl)
    - [inc-build-xterm](https://github.com/ternava/Incremental-build/tree/inc-build-xterm)
    
    Thus, all generated artefacts and obtained data are recorded in a specific branch for each subject system. 
  
  
  - The generated row data, which contain the generated 804 branches per project, or 5 * 804 =  4020 branches in total, are given only in this account because of their large size: https://github.com/inconnue22?tab=repositories. 

  - These data can be generated by following the [Reproduction](https://github.com/ternava/Incremental-build#4-reproduce) steps given below.
  
  - In the main branch, the folder `correctness/` contains the correctness data for each project for
    our full experiment. The notebook `correctness/checker.ipynb` has function
    documentation and how to run the procedure to produce a csv file with the
    result.
  
  - In the `main` branch, the folder `ordering` contains a jupyter notebook `ordering/ExGraph.ipynb` in which you can visualise
    the directed graph that shows the possible build ordering of configurations
    for each system. The graphs are obtained from the csv files in
    `ordering/order`. These csv files were obtained by extracting manually the
    fastest and correct build (clean or incremental) from the build data of Table 2.
  
  - The camera-ready version of the paper is in the `main` branch as `ICSE22_PAPER.pdf` also in the HAL archive at https://hal.archives-ouvertes.fr/hal-03547219.

 ### 3. Branch structure
  
  Each branch has this following folder structure: 
  
  ```yaml
    inc-build-[SystemName] (branch)
    ???
    ???????????? artifacts                                           
    ???   ???   fm-[SystemName]-ib.png
    ???????????? configurations
    ???   ???????????? sample-03
    ???   ???????????? sample-04 
    ???????????? data
    ???   ???????????? rez_sample_03ALL
    ???   ???????????? rez_sample_03I
    ???   ???????????? rez_sample_03II
    ???   ???????????? rez_sample_04ALL
    ???   ???????????? rez_sample_04I
    ???   ???????????? rez_sample_04II
    ???????????? notebooks
    ???   ???????????? rez_sample_03ALL
    ???       ???????????? figures
    ???   ???????????? rez_sample_04ALL
    ???       ???????????? figures
    ???????????? scripts
    ???   Dockerfile 
    ???   README.md
  ```
  
  * _`artifacts`_ folder contains the configuration options model of the system. This model has all compile-time options of the system, including their dependencies, that we used in our experiments. These options are shown by using `$ ./configuration --help` in a system. The model is build using [FeatureIDE](https://featureide.github.io/). This model and FeatureIDE framework is further used to generate the two batches with configurations, given in the folder `configurations`.

  * _`configurations`_ folder contains two subfolders, `sample-03` and `sample-04`. These subfolders contain the **Batch 1** and **Batch 2** with 20 configurations each for the system. These are the used configurations in our experiments. 
    
  * _`data`_ folder contains the generated data after running the scripts given in the `scripts` folder.

  * _`notebooks`_ folder contains the analysed data and generated tables and figures given in the paper, based on the generated data in `data`folder

  * _`scripts`_ folder contains the used scripts to run our experiments. These scripts are also run by using the `Dockerfile`.

  * _`Dockerfile`_ folder contains the instructions to automate the build of experiments and the generated data are made available in a Jupyter notebook.


### 4. REPRODUCE


#### 4.1. Batches of configurations

In each system we have used two batched of configurations. They are available within the folder `configurations` under the names 
- `sample-03` for Batch 1
- `sample-04` for Batch 2

  <details>
    <summary><u>See a</u> <b>screenshot</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->
    
    ![Step 0](screenshots/scrnshot00.png?raw=true)

  </details>

These configurations remain unchanged in order to reproduce our study. 

To switch to a specific batch, please open the file `/scripts/options.py` and follow the instructions given in comments 14-16. For example, [here is](https://github.com/ternava/Incremental-build/blob/98da2825b1b1a759b9377f794bfed5dda8fcb06a/scripts/options.py) the file for the experiments with `curl`.


#### 4.2. Prerequisites

-  Check if you have __docker__ installed by typing `sudo docker --version` in a terminal. If not, then you need to [install it](https://docs.docker.com/get-docker/). If docker is installed, you may need to check whether the docker engine is running by typing `sudo systemctl status docker` in a terminal. If it's not running then start it by typing `sudo systemctl start docker`. 

- Check if you have __git__ installed by typing `git --version` in a terminal. If not, then (optionally) you need to [install it](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

#### 4.3. A QUICK running example


The following steps show how to run a first quick example, by only building the _first three configurations_ from the _batch 1_ in the _x264_ system. The real experiments take more time, as shown in the [table above](https://github.com/ternava/Incremental-build/tree/main#14-required-resources), but the **same exact steps** are used to run them.

- **Step 1:** Open e terminal (you can use the terminal within an IDE, e.g., within Visual Studio Code). 
- **Step 2:** Somewhere in your directory, create a local copy of this project, e.g., by typing `git clone https://github.com/ternava/Incremental-build.git` in a terminal. 
- **Step 3:** By being in the path of this project, enter in the cloned project by typing `cd Incremental-build`. 
- **Step 4:** If you type `git branch -a`, it will show you that you are in the `main` branch. To run experiments with a specific software project, you need to switch to a specific branch (see the [Project Structure](https://github.com/ternava/Incremental-build#2-project-structure)). For instance, to run experiments with _x264_ software system you first need to switch to its branch. To do that, in the terminal you type `git checkout inc-build-x264`. In the following is shown how to run experiments with _x264_, then the same process can be applied for the rest.

  <details>
    <summary><u>See a</u> <b>screenshot</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->
    
    ![Steps 1-4](screenshots/scrnshot01.png?raw=true)

  </details>


- **Step 5:** By being in the `inc-build-x264` branch, build an image from the _Dockerfile_ by typing `sudo docker build -t="imagex264" .` (don't forget the dot at the end, but you are free to change the `imagex264` image name). This step will take up to 10 minutes to be finished. 

  <details>
    <summary><u>See a</u> <b>screenshot</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->
    
    ![Step 5](screenshots/scrnshot02.png?raw=true)

  </details>
  
- **Step 6:** Now you should have the results. 
  
  These following details are optional. In case that you want to see the clean and incremental build configurations of _x264_, you need to run a container from the first before 
  the last image and to enter. First, type `docker images -a`. It will show all built docker images. Take the image ID from the first before the last one, which may look like 
  ~~`60e74b672f3f`~~, and type `docker container run -it` ~~`60e74b672f3f`~~. Then, by typing `cd /github/x264/`and then `git branch -a` it will show all clean and incremental 
  build configurations that are saved in separate branches, just as they are described in our approach in Figure 4 in the original paper. Such branches contain the raw data of 
  our experiments, namely, the Build Time, Binary Size, and Symbols, that we used in our experiments. You can do any detailed observations there. To exit from the container type 
  `Ctrl+Z` and then `Ctrl+D` twice.
  
   <details>
    <summary><u>See a</u> <b>screenshot</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->
    
    ![Step 6](screenshots/scrnshot03.png?raw=true)
  
    ![Step 6](screenshots/scrnshot04.png?raw=true)
  
   - Branches   `x264-00001`,  `x264-00002`, and `x264-00003` are the clean build configurations.
   - Branches  `ix264-00001-00002`, `ix264-00001-00003`, `ix264-00002-00001`, `ix264-00002-00003`, `ix264-00003-00001`, and `ix264-00003-00002` are the incremental build configurations. For example, `ix264-00003-00001` is the incremental build configuration of `00001.config` over the clean buld configuration of `00003.config`.

   </details>
  
    <!-- **Step 6.2:** The clean and incremental build time and executable binary sizes for each configuration are avilable within the `/src/data/` folder in files `buildtime_dc2.csv` (clean build data) and `buildtime_di1.csv` (incremental build data) files. If you want to copy these data from container to the host, you should be outside the container and then type `docker cp <containerId>:/file/path/within/container /host/path/target`. But, you can access these data by using our provided Jupyter notebooks. Hence, you can skip this step. -->
    
- **Step 7:** Run a container from the build image by `docker run --name containerx264 -p 8888:8888 -it imagex264`. (Note: if you have changed the `imagex264` name in **Step 4**, then you should change it here too.)

  <details>
    <summary><u>See a</u> <b>screenshot</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->
    
    ![Step 7](screenshots/scrnshot05.png?raw=true)

  </details>
  
- **Step 8:** To access the notebook, with all the data, open in the browser the given link in the terminal after running the container. ~~For example, http://127.0.0.1:8888/?token=7e13ccabbc597bce788a9ce8114ec4b1ab5e3ad06de75082 (this one will not open on your side).~~ It will open a new tab on your web browser. 

  <details>
    <summary><u>See a</u> <b>screenshot</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->
    
    ![Step 8](screenshots/scrnshot06.png?raw=true)

  </details>
  
- **Step 9:** You will see a directory structure similar to the one provided here in the [Branch Structure](https://github.com/ternava/Incremental-build#3-branch-structure) and within each branch in this project. The results from the Steps 5 and 6 are within the folder `data` in the last two `csv`files. The other folders within this `data` folder contain our original data, which you can use to compare your results. 
  
  <details>
    <summary><u>See a</u> <b>screenshot</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->
    
    ![Step 9](screenshots/scrnshot07.png?raw=true)

  </details>

- **Step 10:** These data are further processed in the folder `notebooks`.  This directory contains 3 other subfolders with 5 notebooks each, which are prefixed with 01-05 because they should run in order. Actually files that begin with 02 and 03 are the most important ones. 

  Open the `rez_sample_03_quicktest` folder and click the `02-CleanBuild.ipynb` file. It will open a new tab with the data from the clean build. In the menubar search for the
  `Kernel -> Restart and run all` and click it. It will refresh the notebook with your data from the run experiment. You need to do this for each notebook in order (the order is
  important!).

  <details>
    <summary><u>See a</u> <b>screenshot</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->

    ![Step 10](screenshots/scrnshot08.png?raw=true)

  </details>

  <details>
    <summary><u>See a</u> <b>screenshot</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->

    ![Step 10](screenshots/scrnshot09.png?raw=true)

  </details>

  <details>
    <summary><u>See a</u> <b>screenshot</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->

    ![Step 10](screenshots/scrnshot10.png?raw=true)

  </details>
    

- **Step 11:** Now, you can compare the obtained data with those that we have provided in Table 2 in the original conference paper. These data are further processed, analysed, and showed in Figures 6 - 8 and Tables 3 - 4 in the paper. For example, compare the Build Time and Binary Size of `x264-00003` with the values in the Table 2 in column `c3` and rows 1 and 4, respectively. The build time is similar and the binary size is identical. 
  
  The `03-IncrementalBuild.ipynb` notebook contains the processed results for the incremental build configurations. And, the `04-CompareCBvsIB.ipynb` notebook contain a comparison of clean and incremental build configurations. 

  <details>
    <summary><u>See a</u> <b>screenshot</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->

    ![Step 11](screenshots/scrnshot11.png?raw=true)
  
    This is Table 2 in the original paper

  </details>
    
  <details>
    <summary><u>See a</u> <b>screenshot</b> (<i>click to expand</i>)</summary>
    <!-- have to be followed by an empty line! -->

    ![Step 11](screenshots/scrnshot12.png?raw=true)
  
    These are the obtained results according to a recent run.

  </details>

- **Step 12:** To stop the container, type `Ctrl+C` twice in the terminal or quit the notebooks.

#### 4.3. A COMPLETE reproduction

The previous example was real, but with only first 3 configurations in the system _x264_.  

The exact same steps should be followed to build all 20 configurations in batch 1 or barch 2 of each 5 systems. This should be done one by one. For instance, to reproduce a complete experiment with _sqlite_ follow these steps: 

- **Step A:** Check if you are in the path of cloned project, that is, within the `Incremental-build` folder (as shown in **Step 3**).
- **Step B:** As mentioned in **Step 4**, you can switch to the sqlite specific branch `git checkout inc-build-sqlite`.
- **Step C:** In whatever 5 project branches you are, you need to decide to experiment with the Batch 1 or Batch 2 of its configurations. To switch between batches, open the file `/scripts/options.py` with an editor or type `nano -l scripts/options.py` in the terminal. Then, as explained in the comment in lines 14-16, you can make the necessary modification in line 18. Save it and exit with `Ctrl+D`.
- **Step D:**  Repeat **Step 5 - Step 12**. 

- Repeat **Steps A - Step C** for each Batch with configurations within a given subject system and for each system.


  **ASIDE NOTE:** As explained in [Required resources](https://github.com/ternava/Incremental-build#14-required-resources), the required disk space is quite considerable. 
  But, after getting the results and saving them in the host for one subject system (or even for one batch of configurations), you can delete containers and images by typing:

  - Delete all containers: `docker rm -f $(docker ps -a -q)`
  - Delete all images: `docker rmi -f $(docker images -a -q)`


### 5. How to REPLICATE the experiments?

In case the replication of experiments is aimed, then several directions are possible. For instance,

  - You may choose to experiment with other new subject systems. Then, first make sure that it has compile-time configuration options. Prepare the configurations that you want to test, in the same format as those given in the folder `configurations`. Next, create a similar branch, and copy-paste the structure of another existing branche in this project. Adapt it, as we did for current projects, including the Dockerfile.
  
  - Another alternative for replication is to experiment with a larger or different number of configurations in our 5 chosen subject systems. In that case, you need just to provide a new set with configurations for them and to add it in the `configurations` folder of that particular project. Then, repeat **Steps A - Step C**.

