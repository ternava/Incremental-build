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

RUN cd ..
RUN mkdir github
WORKDIR /github/
RUN git clone https://github.com/mirror/x264.git
WORKDIR /github/x264/
#RUN git reset --hard ae03d92
#RUN git checkout ae03d92

# Make clean build of x264
RUN python3 /src/scripts/makeclean_single.py
RUN python3 /src/scripts/makeclean_sample.py
# Incremental build of x264
RUN python3 /src/scripts/incremental_sample.py

# Show the obtained results from the make clean and incremental build of x264
WORKDIR /src/notebooks

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
#ENV TINI_VERSION v0.6.0
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
#RUN chmod +x /usr/bin/tini
#ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]