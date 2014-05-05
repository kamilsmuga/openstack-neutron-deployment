#!/usr/bin/env python

# Script to manage OpenStack Neutron cluster set up via Vagrant
# Git: https://github.com/kamilsmuga/openstack-neutron-deployment
# Author: Kamil Smuga smugakamil@gmail.com

from time import sleep
import sys
import os
import argparse
import subprocess

CURRENT_DIR = os.getcwd()

def network(command):
	os.chdir(CURRENT_DIR+'/network-node/')
	subprocess.call("vagrant "+command, shell=True)

def controller(command):
	os.chdir(CURRENT_DIR+'/controller-node/')
	subprocess.call("vagrant "+command, shell=True)

def compute(command):
	os.chdir(CURRENT_DIR+'/compute-node/')
	subprocess.call("vagrant "+command, shell=True)

def main(argv):

    parser = argparse.ArgumentParser(description='Manage OpenStack Neutron cluster set up via Vagrant')
    parser.add_argument('commands', nargs='+', help='[up, destroy, halt, suspend, ssh]')
    parser.add_argument('-n', '--node', dest='node', help='Specify a node when attempting to ssh.')

    args = parser.parse_args()

    for command in args.commands:
	if command == 'up' or command == 'destroy' or command == 'halt' or command == 'suspend':
		if command == 'destroy':
			command = 'destroy -f'
		network(command)
		controller(command)
		compute(command)
	elif command == 'ssh':
		if args.node:
			if args.node == 'compute':
				compute(command)
			elif args.node == 'network':
				network(command)	
			elif args.node == 'controller':
				controller(command)
			else:
				print 'Need to specify a valid node to ssh. Node names: network, controller, compute'
                        	sys.exit(1)
		else:
			print '-n (--node) flag is required when attempting to ssh'
                        sys.exit(1)
	else:
		print "Didn't recognize your command. Try one of those: up, destroy, halt, suspend, ssh"

if __name__ == "__main__":
    main(sys.argv[1:])
