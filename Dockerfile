# Base image as Fedora
FROM fedora:33

######################### START: Set up environment for sqlite ######################
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

######################### END: Set up environment for sqlite ######################

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
RUN git clone https://github.com/sqlite/sqlite.git
WORKDIR /github/sqlite/
#RUN git reset --hard version-3.35.4
#RUN git checkout version-3.35.4

# Make clean build of sqlite
RUN python3 /src/scripts/makeclean_single.py
RUN python3 /src/scripts/makeclean_sample.py
# Incremental build of sqlite
RUN python3 /src/scripts/incremental_sample.py

# Show the obtained results from the make clean and incremental build of sqlite
WORKDIR /src/notebooks

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
#ENV TINI_VERSION v0.6.0
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
#RUN chmod +x /usr/bin/tini
#ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]