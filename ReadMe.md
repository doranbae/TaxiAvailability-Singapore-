#Taxi Availability in Singapore


Please add your public key while provisioning the VMs (slcli vs create ... --key KEYID) so that you can login from your client without a password.

Get 2 CPUs, 4G of RAM, 1G private / public NICS and two disks: 25G and 100G local the idea is to use the 100G disk for HDFS data and the 25G disk for the OS and housekeeping.

For the master, you might do something like this:

slcli vs create --datacenter=sjc01 --hostname=master --domain=mids --billing=hourly --key=<mykey> --cpu=2 --memory=4096 --disk=25 --disk=100 --network=1000 --os=CENTOS_LATEST_64
VM Configuration

Note: Instructions in this section are to be performed on each node unless otherwise stated.

Hosts file

Log into VMs (all 3 of them) and update /etc/hosts/ with each system's public IP addresses (note that it's preferred to use private IPs for this communication instead, but that complicates use of Hadoop's UIs. For this assignment, public IPs will do. Here's my hosts file:

