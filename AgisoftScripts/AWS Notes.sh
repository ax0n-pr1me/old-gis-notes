# Create p2.8xlarge instance with 64Gb SSD
instance-id i-06fcece9cce93eed5

# Default VPC at 
IPv4 CIDR: 172.31.0.0/16
VPC ID: vpc-0b53ca6f

# Create 9Tb EBS volume
vol-09d658a4a0fdc13ea
9313 GiB

# login
ssh -i ".ssh/c0ba1t-key.pem" ubuntu@52.38.18.8

# attach EBS volume
aws ec2 attach-volume --volume-id vol-09d658a4a0fdc13ea --instance-id i-06fcece9cce93eed5 --device /dev/xvdb

# format and mount EBS drive to `/engineering`
lsblk
sudo file -s /dev/xvdb
sudo mkfs -t ext4 /dev/xvdb
sudo mkdir /engineering
sudo mount /dev/xvdb /engineering/
cd /engineering
df -h .

# auto mount on reboot
# Open /etc/fstab file and make the following entry
/dev/xvdb       /engineering   ext4    defaults,nofail

# check with the following command
sudo mount -a

# install nvidia driver
wget http://us.download.nvidia.com/tesla/396.44/NVIDIA-Linux-x86_64-396.44.run

# update linux and reboot
sudo apt-get update -y
sudo apt-get upgrade -y linux-aws
sudo reboot

# install gcc compiler
sudo apt-get install -y gcc make linux-headers-$(uname -r)

sudo /bin/sh ./NVIDIA-Linux-x86_64*.run

sudo reboot

# check install and set performance tweaks
nvidia-smi -q | head
sudo nvidia-persistenced
sudo nvidia-smi --auto-boost-default=0
sudo nvidia-smi -ac 2505,875

#install desktop light - might not be required because had to install QT anyway
sudo apt-get install --no-install-recommends ubuntu-desktop

#install Qt
wget http://download.qt.io/official_releases/online_installers/qt-unified-linux-x64-online.run

#install and license photoscan
wget http://download.agisoft.com/photoscan-pro_1_4_3_amd64.tar.gz
tar xvzf photoscan-pro_1_4_3_amd64.tar.gz
photoscan-pro/photoscan.sh --activate TGN25-21RGK-UM9NG-UK49O-V55ZO


# run sparse in Tmux
tmux new -s sparse
sudo 
#ctrl+b d
tmux a -t sparse

sudo photoscan-pro/photoscan.sh -platform offscreen -r sparse.py


# success! - running sparse cloud on p2 instance :)





######## set up NVIDIA on G3 ##########
#
#aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
#
#sudo apt-get update -y
#
#sudo apt-get upgrade -y linux-aws
#
#sudo reboot
#
### login again
#
#sudo apt-get install -y gcc make linux-headers-$(uname -r)
#
## aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
#
#sudo /bin/sh ./NVIDIA-Linux-x86_64*.run
#
#sudo reboot
#
#nvidia-smi -q | head
#
#
## optimize
#
#sudo cp /etc/nvidia/gridd.conf.template /etc/nvidia/gridd.conf
#
#FeatureType=0
#IgnoreSP=TRUE
#
#sudo reboot
#
## persistant
#
#sudo nvidia-persistenced
#
#sudo nvidia-smi --auto-boost-default=0
#
#sudo nvidia-smi -ac 2505,1177


# after login - to check on progress of sync
watch -n .1 tail /home/ubuntu/nohup.out


