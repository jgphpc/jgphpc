# https://user.cscs.ch/tools/containers/advanced_shifter/
# docker build -t jg -f ./Dockerfile .
FROM nvidia/cuda:latest

# https://packages.ubuntu.com
RUN apt-get -y update && \
    apt-get install -y \
    apt-utils       \
    libice6         \
    libsm6          \
    libx11-6        \
    libxext6        \
    libxrender1     \
    libfontconfig1  \
    libfreetype6    \
    libxpm4

# Define environment variable
ENV DDTPATH /scratch/snx3000/piccinal/RT/shifter/ddt/18.3/bin

# Run app.py when the container launches
#CMD ["python", "app.py"]
