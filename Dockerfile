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
                        meson \
                        ninja-build \
                        pkg-config \
                        texinfo \
                        wget \
                        yasm

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
RUN git clone https://github.com/xz-mirror/xz.git
WORKDIR /github/xz/
#RUN git reset --hard e7da44d
#RUN git checkout e7da44d

# Make clean build of xz
RUN python3 /src/scripts/makeclean_single.py
RUN python3 /src/scripts/makeclean_sample.py
# Incremental build of xz
RUN python3 /src/scripts/incremental_sample.py

# Show the obtained results from the make clean and incremental build of xz
WORKDIR /src/notebooks

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
#ENV TINI_VERSION v0.6.0
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
#RUN chmod +x /usr/bin/tini
#ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]