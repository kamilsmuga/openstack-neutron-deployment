openstack-neutron-deployment
============================

Vagrant auto deployment of three-node architecture with OpenStack Networking (neutron)

![Alt text](http://docs.openstack.org/icehouse/install-guide/install/apt/content/figures/1/figures/installguide_arch-neutron.png "Openstack three-node architecture with Neutron networking")

## Deployment set up as documented here:
http://docs.openstack.org/icehouse/install-guide/install/apt/content/ch_basics.html

## Cluster operations control
```
usage: cluster.py [-h] [-n NODE] commands [commands ...]

Manage OpenStack Neutron cluster set up via Vagrant

positional arguments:
  commands [up, destroy, halt, suspend, ssh]

optional arguments:
  -h, --help            show this help message and exit
  -n NODE, --node NODE  Specify a node when attempting to ssh.
```

## Config structure

#### controller-node
1. puppet/manifests - puppet manifest files
  * network.pp - network manifest to manipulate /etc/hosts file

#### compute-node
1. puppet/manifests - puppet manifest files
  * network.pp - network manifest to manipulate /etc/hosts file
  
#### network-node
1. puppet/manifests - puppet manifest files
  * network.pp - network manifest to manipulate /etc/hosts file
2. shell/
  * network.sh - overrides eth3 interface configuration to IP-less external interface (point 3 http://docs.openstack.org/icehouse/install-guide/install/apt/content/basics-neutron-networking-network-node.html)
