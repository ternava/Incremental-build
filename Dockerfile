# Base image as Fedora
FROM fedora:33

######################### START: Set up environment for curl ######################
RUN sudo dnf update -y
RUN sudo dnf groupinstall -y "Development Tools" "Development Libraries"
RUN sudo dnf install -y nasm \
                        libtool \
                        autoconf \
                        automake \
                        cmake \
                        git-core \
                        pkg-config \
                        wget

# Installed some of the missed libraries for curl
RUN sudo dnf install -y brotli \
                        mbedtls \
                        libgsasl \
                        libssh2 \
                        nghttp2 \
                        fish \
                        gzip \
                        lcov

# few more libraries are not installed because they are platform dependent. 
# They are: aix-soname, winssl, schannel, darwinssl, secure-transport, amissl, 
# egd-socket, random, wolfssl, mesalink, bearssl, rustls, ca-bundle, ca-path, 
# ca-fallback, wolfssh, librtmp, winidn, ngtcp2, nghttp3, quiche, hyper, 

######################### END: Set up environment for curl ######################

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
#RUN git clone https://github.com/curl/curl.git
#WORKDIR /github/curl/
#RUN git reset --hard c34bd93

RUN wget https://github.com/curl/curl/archive/curl-7_78_0.zip -O /tmp/curl.zip
RUN unzip /tmp/curl.zip -d /tmp/
RUN mv /tmp/curl-curl-7_78_0/ /github/curl/
WORKDIR /github/curl/
RUN git init 
RUN git config --global user.email "icse22@gmail.com" 
RUN git config --global user.name "icse22" 
RUN git add -f * 
RUN git commit -m "Initial project version"

# The ignored files, if exists, are enabled to be commited
RUN python3 /src/scripts/is_gitignore.py

# Make clean build of curl
RUN python3 /src/scripts/makeclean_single.py
RUN python3 /src/scripts/makeclean_sample.py
# Incremental build of curl
RUN python3 /src/scripts/incremental_sample.py

# Show the obtained results from the make clean and incremental build of curl
WORKDIR /src/notebooks
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]