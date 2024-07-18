# (c) 2024, Gijs Entius <g.m.entius@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import annotations

from ansible.errors import AnsibleFilterError
from ansible.utils.display import Display

display = Display()

def image_name_from_url(url: str):
    return url.split("/")[-1]

def image_hash_from_url(url_data, image_name):
    # find hash in file with hashes
    url_data = url_data.split("\n")
    for line in url_data:
        if image_name in line:
            return line.split(" ")[0]
    raise AnsibleFilterError("Checksum could not be found")

class FilterModule(object):
    ''' Jinja2 filters '''

    def filters(self):
        return {
            'image_hash_from_url': image_hash_from_url,
            'image_name_from_url': image_name_from_url,
        }
