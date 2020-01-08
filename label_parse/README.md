# NVIDIA DIGITS on Ubuntu 18.04

## Install Docker

https://docs.docker.com/install/linux/docker-ce/ubuntu/

```{bash}

sudo apt-get remove docker docker-engine docker.io containerd runc

# Install dependencies

sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

# add the key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] \
   https://download.docker.com/linux/ubuntu/dists/bionic/stable/ \
   stable"

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo dockerd --debug

sudo ip link add name docker0 type bridge
sudo ip addr add dev docker0 172.17.0.1/16

sudo dpkg --remove --force-remove-reinstreq docker-ce
sudo apt-get install docker-ce
sudo apt-get install docker-compose

sudo docker run hello-world

sudo usermod -a -G docker $USER # requires a log out to take effect

docker system info
docker system prune -a -f

```

### Error Notes

```
Setting up docker-ce (5:19.03.5~3-0~ubuntu-bionic) ...
Job for docker.service failed because the control process exited with error code.
See "systemctl status docker.service" and "journalctl -xe" for details.
invoke-rc.d: initscript docker, action "start" failed.
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: activating (auto-restart) (Result: exit-code) since Thu 2019-12-26 10:21:34 MST; 12ms ago
     Docs: https://docs.docker.com
  Process: 21488 ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock (code=exited, status=1/FAILURE)
 Main PID: 21488 (code=exited, status=1/FAILURE)
dpkg: error processing package docker-ce (--configure):
 installed docker-ce package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 docker-ce
E: Sub-process /usr/bin/dpkg returned an error code (1)

```

Needed to create bridge network. See above ip commands





## Install Nvidia-Docker

https://github.com/NVIDIA/nvidia-docker

distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker










# Build Docker image for Digits from NVIDIA GPU Cloud

```s

docker login nvcr.io
# Username: $oauthtoken
# Password: dHFtc2IyMGo5NWkyMmFlbDhrdnAycW80MHI6ODZiZDMyNTctMDU4My00Zjg4LThhOWUtNzZmZGMyYWVmMTk2

docker pull nvcr.io/nvidia/digits:18.10
docker pull nvcr.io/nvidia/digits:19.12-caffe

nvidia-docker run -it --rm -v \
/home/om/data/kitti:/data/kitti \
--name digits -d -p 8888:5000 nvcr.io/nvidia/digits:18.10

docker run -it --rm -v \
/home/om/data/kitti:/data/kitti \
--name digits -d -p 8888:5000 nvcr.io/nvidia/digits:19.12-caffe-py3


nvidia-docker run -it \
-v /home/om/data/kitti:/data/kitti \
--name digits -d \
-p 8888:5000 -p 3000:8888 \
nvcr.io/nvidia/digits:19.10-caffe


jupyter notebook --ip=0.0.0.0 --no-browser --allow-root



```

## References



https://docs.nvidia.com/deeplearning/digits/digits-container-getting-started/index.html
https://devblogs.nvidia.com/detectnet-deep-neural-network-object-detection-digits/
https://ngc.nvidia.com/catalog/all
https://docs.nvidia.com/deeplearning/digits/digits-release-notes/rel_19-10.html#rel_19-10
https://www.nvidia.com/en-us/gpu-cloud/containers/ 
https://docs.google.com/presentation/d/1UeKXVgRvvxg9OUdh_UiC5G71UMscNPlvArsWER41PsU/edit#slide=id.gc2fcdcce7_216_0
https://docs.google.com/presentation/d/1HxGdeq8MPktHaPb-rlmYYQ723iWzq9ur6Gjo71YiG0Y/edit#slide=id.gc2fcdcce7_216_0
https://developer.nvidia.com/digits














https://ngc.nvidia.com/catalog/containers/nvidia%2Fdigits

https://github.com/NVIDIA/DIGITS

https://docs.nvidia.com/deeplearning/digits/digits-release-notes/rel_18.10.html#rel_18.10

https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#cuda-compatibility-and-upgrades

