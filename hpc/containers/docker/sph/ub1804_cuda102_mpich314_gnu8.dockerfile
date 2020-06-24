FROM nvidia/cuda:10.2-devel-ubuntu18.04
#{{{ FROM ubuntu:bionic
#FROM ethcscs/mpich:ub1804_cuda101_mpi314_osu
#docker pull nvidia/cuda:10.1-devel
#MAINTAINER Giorgio

# Ubuntu/18.04.3
# gnu/7.4.0
# MPICH/3.3a2

# https://wiki.ubuntu.com/Releases
# https://gitlab.com/nvidia/container-images/cuda/blob/master/doc/supported-tags.md
#
# DD=Dockerfile.ub1804_mpich314
# VV=nemo/ub1804:mpich314
# docker build -f ./$DD -t $VV .
# docker run --rm -it $VV bash
# mpirun -np 2 /usr/local/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_bw
#
# mac: docker image save $VV -o nemo.tar # + scp
# dom: sarus load nemo.tar nemo/ub1804
#
# #VV=sphexa/mpich:ub1804_cuda101_mpi314_sphexa_ci
# #docker build -f ./$DD -t $VV --build-arg branchname=master .
# docker push $VV
#
# docker run --rm $VV
# docker run --rm $VV bash -c "./gnu7/omp.app -s 1 -n 10"
# docker run --rm $VV bash -c "mpirun -np 2 ./gnu7/mpi+omp.app -s 1 -n 20"
# docker run --rm -it $VV bash
# docker run $VV cat /etc/os-release
# FROM ethcscs/mpich:ub1804_cuda101_mpi314_osu
# PS1="\[\033[31m\]\u:\w/$ \[\e[0;36m\]"
# vim.tiny ~/.bashrc
#}}}

#{{{ apt:
RUN apt update --quiet \
    && apt install -y file \
                 g++-8 \
                 gcc-8 \
                 make \
                 gdb \
                 strace \
                 wget \
                 unzip \
                 --no-install-recommends \
    && ln -fs /usr/bin/make /usr/bin/gmake
#{{{ apt
# RUN apt-get update \
#     && apt-get install -y sudo
# # add a new user
# RUN adduser docker-nemo --gecos "Docker Nemo,1,0000,0001" --disabled-password
# RUN echo "docker-nemo:password" | chpasswd \
#     && usermod -aG sudo docker-nemo
# # update and install dependencies
# RUN apt-get install -y \
#             software-properties-common \
#             wget \
#             locate \
#             && add-apt-repository -y ppa:ubuntu-toolchain-r/test \
#             && apt-get update \
#             && apt-get install -y \
#             make \
#             git \
#             curl \
#             vim \
#             && apt-get install -y cmake \
#             && apt-get install -y \
#             gcc \
#             g++ \
#             gfortran
#}}}
#}}}

#{{{ mpich/3.1.4:
COPY mpich-3.1.4.tar.gz /tmp/M/
RUN echo \
    && mkdir -p /tmp/M ;cd /tmp/M \
    # && wget -q http://www.mpich.org/static/downloads/3.1.4/mpich-3.1.4.tar.gz \
    && tar xf mpich-3.1.4.tar.gz \
    && cd mpich-3.1.4 \
    && ./configure --enable-cxx --disable-fortran --enable-g=none CXX=g++-8 CC=gcc-8 --prefix=/usr \
    && make -j6 \
    && make install \
    && ldconfig 
#no!:    && apt install --quiet -y --no-install-recommends libmpich-dev mpich wget make \
#    && apt install --quiet -y --no-install-recommends libmpich-dev mpich wget make \
#{{{ mpich/ubuntu:
# RUN apt-get install -y \
#     libmpich-dev \
#     libmpich12 \
#     mpich \
#     mpich-doc
#}}}

#{{{ osu-micro-benchmarks:
# RUN cd /tmp \
#     && wget http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-5.6.2.tar.gz \
#     && tar xf osu-micro-benchmarks-5.6.2.tar.gz \
#     && cd osu-micro-benchmarks-5.6.2 \
#     && ./configure CC=$(which mpicc) \
# #    && ./configure --prefix=/usr/local CC=$(which mpicc) CFLAGS=-O3 \
#     && make -j2 \
#     && make install \
#     && cd .. \
#     && rm -rf osu-micro-benchmarks-5.6.2*
#}}}
#}}}

