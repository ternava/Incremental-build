# Base image as Fedora
FROM fedora:33

######################### START: Set up environment for x264 ######################
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
                        meson \
                        ninja-build \
                        pkg-config \
                        texinfo \
                        wget \
                        yasm

# Install the ffmpeg library for lavf support
RUN sudo dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
RUN sudo dnf -y install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
RUN sudo dnf -y install ffmpeg
RUN sudo dnf -y install ffmpeg-devel
RUN whereis ffmpeg

# Install the ffms2 library for ffms support
WORKDIR /usr/lib/
RUN git clone -b 2.23 https://github.com/FFMS/ffms2.git
RUN cd ffms2
WORKDIR /usr/lib/ffms2
RUN ./configure
RUN make install

# Install the lsmash library for mp4 support
WORKDIR /usr/lib
RUN git clone https://github.com/l-smash/l-smash
RUN cd l-smash
WORKDIR /usr/lib/l-smash
RUN ./configure
RUN make install
######################### END: Set up environment for x264 ######################

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

#RUN cd ..
WORKDIR /
RUN mkdir github
WORKDIR /github/
#RUN git clone https://github.com/mirror/x264.git
#WORKDIR /github/x264/
#RUN git reset --hard ae03d92
#RUN git checkout ae03d92

RUN wget https://github.com/mirror/x264/archive/ae03d92.zip -O /tmp/x264.zip
RUN unzip /tmp/x264.zip -d /tmp/
RUN mv /tmp/x264-ae03d92b52bb7581df2e75d571989cb1ecd19cbd/ /github/x264/
WORKDIR /github/x264/
RUN git init 
RUN git config --global user.email "anonymous22@gmail.com" 
RUN git config --global user.name "anonymous22" 
RUN git add -f * 
RUN git commit -m "Initial project version"

# The ignored files, if exists, are enabled to be commited
RUN python3 /src/scripts/is_gitignore.py

# Make clean build of x264
#RUN python3 /src/scripts/makeclean_single.py
RUN python3 /src/scripts/makeclean_sample.py
# Incremental build of x264
RUN python3 /src/scripts/incremental_sample.py

# Show the obtained results from the make clean and incremental build of x264
WORKDIR /src/notebooks
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]