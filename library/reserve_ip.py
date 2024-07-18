#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: nextip

short_description: This is a module to find a new ip address in a subnet 

version_added: "1.0.0"

description: This module finds the next available ip address in a subnet by using ping 

options:
    subnet:
        description: Subnet to search for an available ip address in cidr notation
        required: true
        type: str

author:
    - Gijs Entius (@gijsentius)
'''

EXAMPLES = r''' 
- name: Find the first available ip
  nextip:
   subnet: 192.168.1.0/24
'''

RETURN = r'''
# These are examples of possible return values
ip:
    description: The output ip the module generates
    type: str
    returned: always
    sample: '192.168.1.42'
'''

from ansible.module_utils.basic import AnsibleModule
import ipaddress
import subprocess

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        subnet=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        ip=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    subnet = module.params['subnet']
    
    # Strip the first and last address of the ips in a subnet
    ips_in_subnet = [str(ip) for ip in ipaddress.IPv4Network(subnet)][1:-1]
    for ip in ips_in_subnet:
        command = ['ping', '-c', '1', '-W', '1', ip]
        if subprocess.call(command) != 0:
            result['ip'] = ip
            break

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
