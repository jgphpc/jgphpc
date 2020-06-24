FROM ub1804_cuda102_mpich314_gnu8:latest
# {{{ with docker:
# git clone https://github.com/unibas-dmi-hpc/SPH-EXA_mini-app.git SPH-EXA_mini-app.git
# docker build -f ./ub1804_cuda102_mpich314_gnu8+sph.dockerfile -t ub1804_cuda102_mpich314_gnu8:sph .
# docker run --rm -it ub1804_cuda102_mpich314_gnu8:sph bash
# }}}
# {{{ with buildah:
# salloc -Cgpu,contbuild -N1
# RR='--root=/scratch/local/$USER/buildah_root --runroot=/scratch/local/$USER/buildah_runroot --storage-driver=vfs'
# ---
# srun buildah pull $RR docker-archive:/scratch/snx3000tds/piccinal/CONTAINERS/sph/ub1804_cuda102_mpich314_gnu8.tar
# srun buildah images $RR
# srun buildah tag $RR 1543ef60da17 ub1804_cuda102_mpich314_gnu8:latest
# srun buildah images $RR
#
# git clone https://github.com/unibas-dmi-hpc/SPH-EXA_mini-app.git SPH-EXA_mini-app.git
# srun buildah bud $RR --tag=ub1804_cuda102_mpich314_gnu8:sph -f \
# ~/jgphpc.git/hpc/containers/docker/sph/ub1804_cuda102_mpich314_gnu8+sph.dockerfile .
#
# srun buildah push $RR ub1804_cuda102_mpich314_gnu8:sph \
# docker-archive:/scratch/local/$USER/buildah_runroot/eff.tar
# #SLOW! srun buildah push $RR ub1804_cuda102_mpich314_gnu8:sph docker-archive:$PWD/eff.tar
# 
# cp /scratch/local/$USER/buildah_runroot/eff.tar ub1804_cuda102_mpich314_gnu8+sph.tar
# ---
# srun buildah pull $RR docker-archive:mpich_osu.tar
# srun buildah tag $RR ef39eecb1319 mpich_osu:latest
# srun buildah $RR images
## REPOSITORY            TAG      IMAGE ID       CREATED        SIZE
## localhost/mpich_osu   latest   ef39eecb1319   12 hours ago   294 MB
# }}}

COPY SPH-EXA_mini-app.git /home/SPH-EXA_mini-app/

# TODO: install git # git log -n1
RUN cd /home/SPH-EXA_mini-app; ls -la; pwd; \
    rm -fr .git; \
    mkdir -p /home/bin/gnu8; \
    mpichversion; \
    mpicxx --version; \
    mpicxx -I. -I./include -std=c++14 -g -O2 -DUSE_MPI -DNDEBUG \
    src/sqpatch/sqpatch.cpp -o /home/bin/gnu8/mpi+omp.app

WORKDIR /home/bin/gnu8/

CMD ["/home/bin/gnu8/mpi+omp.app", "-s", "0", "-n", "20"]

# {{{ https://github.com/containers/buildah/tree/master/docs/tutorials
# new=$(srun buildah from scratch)
# RR='--root=/scratch/local/$USER/buildah_root --runroot=/scratch/local/$USER/buildah_runroot --storage-driver=vfs'
# srun buildah containers $RR
# srun buildah images $RR
# scratchmnt=$(srun buildah mount $RR $new)
## chown /scratch/local/$USER/buildah_root/vfs: operation not permitted
# srun buildah run $RR $new bash
## error reading build container "working-container-1": error reading build container: container not known
# srun buildah inspect $new
# buildah commit $newcontainer fedora-bashecho
# buildah images
# buildah inspect --type=image fedora-bashecho
# srun buildah rm working-container # $new
# ---
# srun buildah pull $RR docker-archive:mpich_osu.tar
# srun buildah tag $RR ef39eecb1319 mpich_osu:latest
# srun buildah $RR images
## REPOSITORY            TAG      IMAGE ID       CREATED        SIZE
## localhost/mpich_osu   latest   ef39eecb1319   12 hours ago   294 MB
# srun buildah bud $RR --tag=mpich_osu:cat -f thisfile
# }}}
