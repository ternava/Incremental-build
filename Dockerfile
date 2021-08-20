# Base image as Fedora
FROM fedora:33

######################### START: Set up environment for sqlite ######################
RUN sudo dnf update -y
RUN sudo dnf groupinstall -y "Development Tools" "Development Libraries"
RUN sudo dnf install -y libtool \
                        autoconf \
                        automake \
                        cmake \
                        git-core \
                        pkg-config \
                        libass-devel \
                        libva-devel \
                        libvdpau-devel \
                        libvorbis-devel \
                        wget

######################### END: Set up environment for sqlite ######################

# Install python, pandas, and jupyter
RUN dnf install -y python3.6 python3-pip python3-devel python3-pandas
RUN python3 -m pip install gitpython

RUN sudo dnf install numpy python3-matplotlib
RUN pip3 install jupyterlab

RUN mkdir src
WORKDIR /src/
COPY . .

RUN cd ..
RUN mkdir github
WORKDIR /github/
#RUN git clone https://github.com/sqlite/sqlite.git
#WORKDIR /github/sqlite/
#RUN git reset --hard version-3.35.4
#RUN git checkout version-3.35.4

RUN wget https://github.com/sqlite/sqlite/archive/version-3.35.4.zip -O /tmp/sqlite.zip
RUN unzip /tmp/sqlite.zip -d /tmp/
RUN mv /tmp/sqlite-version-3.35.4/ /github/sqlite/
WORKDIR /github/sqlite/
RUN git init 
RUN git config --global user.email "anonymous22@gmail.com" 
RUN git config --global user.name "anonymous22" 
RUN git add -f * 
RUN git commit -m "Initial project version"

# The ignored files, if exists, are enabled to be commited
RUN python3 /src/scripts/is_gitignore.py

# Make clean build of sqlite
RUN python3 /src/scripts/makeclean_single.py
RUN python3 /src/scripts/makeclean_sample.py
# Incremental build of sqlite
RUN python3 /src/scripts/incremental_sample.py

# Show the obtained results from the make clean and incremental build of sqlite
WORKDIR /src/notebooks
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]