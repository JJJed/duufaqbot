import requests
import re

import requests
import re

url = "https://discordrollout.nekos.sh/api/data/status"


def get_info():
    nitro_info = ""
    nonnitro_info = ""

    response = requests.request("GET", url)

    match = re.search(r'"nitro":"([^"]+)"', response.text)
    if match:
        nitro_info = match.group(1)

    match = re.search(r'"nonnitro":"([^"]+)"', response.text)
    if match:
        nonnitro_info = match.group(1)

    complete = nitro_info + "|" + nonnitro_info

    return complete
