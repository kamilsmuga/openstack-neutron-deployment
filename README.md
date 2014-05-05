openstack-neutron-deployment
============================

Vagrant auto deployment of three-node architecture with OpenStack Networking (neutron)

![Alt text](http://docs.openstack.org/icehouse/install-guide/install/apt/content/figures/1/figures/installguide_arch-neutron.png "Openstack three-node architecture with Neutron networking")

### Deployment set up as documented here:
http://docs.openstack.org/icehouse/install-guide/install/apt/content/ch_basics.html

### Config structure

#### controller-node
1. shell/ - shell provisioning scripts
  * network.sh - sets up default gateway through `route` tool. Note: does not work with `vagrant reload`. Have to use `vagrant provision` to have correctly set up default gateway 
2. puppet/manifests - puppet manifest files
  * network.pp - network manifest to manipulate /etc/hosts file
