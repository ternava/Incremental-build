# Base image as Fedora
FROM fedora:33

######################### START: Set up environment for xterm ######################
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

# The needed libraries to build xterm: 
RUN sudo dnf install -y libXaw-devel

RUN wget https://download.savannah.gnu.org/releases/freetype/freetype-2.10.1.tar.gz
RUN tar xvfz freetype-2.10.1.tar.gz
WORKDIR /freetype-2.10.1/
RUN ./configure --prefix=/usr/local/freetype/2_10_1 --enable-freetype-config
RUN make
RUN make install

######################### END: Set up environment for xterm ######################

WORKDIR /
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
#RUN git clone https://github.com/ThomasDickey/xterm-snapshots.git
#WORKDIR /github/xterm/
#RUN git reset --hard xterm-368
#RUN git checkout xterm-368

RUN wget https://github.com/ThomasDickey/xterm-snapshots/archive/xterm-368.zip -O /tmp/xterm.zip
RUN unzip /tmp/xterm.zip -d /tmp/
RUN mv /tmp/xterm-snapshots-xterm-368/ /github/xterm/
WORKDIR /github/xterm/
RUN git init 
RUN git config --global user.email "anonymous22@gmail.com" 
RUN git config --global user.name "anonymous22" 
RUN git add -f * 
RUN git commit -m "Initial project version"

# The ignored files, if exists, are enabled to be commited
RUN python3 /src/scripts/is_gitignore.py

# Make clean build of xterm
#RUN python3 /src/scripts/makeclean_single.py
RUN python3 /src/scripts/makeclean_sample.py
# Incremental build of xterm
RUN python3 /src/scripts/incremental_sample.py

# Show the obtained results from the make clean and incremental build of xterm
WORKDIR /src/notebooks
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]