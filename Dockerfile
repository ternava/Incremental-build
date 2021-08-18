# Base image as Fedora
FROM fedora:33

######################### START: Set up environment for xz ######################
RUN sudo dnf update -y
RUN sudo dnf groupinstall -y "Development Tools" "Development Libraries"
RUN sudo dnf install -y nasm \
                        libtool \
                        autoconf \
                        automake \
                        cmake \
                        git-core \
                        libass-devel \
                        libva-devel \
                        libvdpau-devel \
                        libvorbis-devel \
                        pkg-config \
                        texinfo \
                        wget \
                        gettext-devel

######################### END: Set up environment for xz ######################

# Install dependencies for python, pandas, and jupyter
RUN dnf install -y python3.6 python3-pip python3-devel python3-pandas
RUN python3 -m pip install gitpython
# RUN pip3 -q install pip --upgrade
# RUN python3 -m pip install --user

RUN sudo dnf install numpy python3-matplotlib
RUN pip3 install jupyterlab

RUN mkdir src
WORKDIR /src/
COPY . .

RUN cd ..
RUN mkdir github
WORKDIR /github/
#RUN git clone https://github.com/xz-mirror/xz.git
#WORKDIR /github/xz/
#RUN git reset --hard e7da44d
#RUN git checkout e7da44d

RUN wget https://github.com/xz-mirror/xz/archive/e7da44d.zip -O /tmp/xz.zip
RUN unzip /tmp/xz.zip -d /tmp/
RUN mv /tmp/xz-e7da44d5151e21f153925781ad29334ae0786101/ /github/xz/
WORKDIR /github/xz/
RUN git init 
RUN git config --global user.email "anonymous22@gmail.com" 
RUN git config --global user.name "anonymous22" 
RUN git add -f * 
RUN git commit -m "Initial project version"

# The ignored files, if exists, are enabled to be commited
RUN python3 /src/scripts/is_gitignore.py

# Make clean build of xz
RUN python3 /src/scripts/makeclean_single.py
RUN python3 /src2/scripts/makeclean_sample.py
# Incremental build of xz
RUN python3 /src2/scripts/incremental_sample.py

# Show the obtained results from the make clean and incremental build of xz
WORKDIR /src/notebooks
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]