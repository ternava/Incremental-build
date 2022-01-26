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


### What these artifacts do


### How to obtain the artifact package

### How to replicate the results presented in the paper

- (for the results in the paper) First switch to the right branch, then run the Dockerfile. (what are the storage requirements?)



  

  
  
- Used dockerfiles:
- Generated clean and incremental builds:
- Obtained data:



