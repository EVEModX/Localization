#!/usr/bin/env python

import requests
import re
import hashlib

def download_fsd_pickle():
    build = requests.get("https://binaries.eveonline.com/eveclient_TQ.json", timeout=10).json()['build']

    client_index = requests.get("https://binaries.eveonline.com/eveonline_{}.txt".format(build), timeout=10).text

    resfileindex_path = re.search(r'^app:\/resfileindex\.txt,(\w{2}\/\w+),', client_index, flags=re.MULTILINE).group(1)
    resfileindex = requests.get("https://binaries.eveonline.com/" + resfileindex_path, timeout=10).text

    match = re.search(r'^res:\/localizationfsd\/localization_fsd_en-us\.pickle,(\w{2}\/\w+),(\w+),(\d+)', resfileindex, flags=re.MULTILINE)
    fsd_path = match.group(1)
    fsd_md5 = match.group(2)

    fsd_pickle = requests.get("https://resources.eveonline.com/" + fsd_path, timeout=60).content

    assert hashlib.md5(fsd_pickle).hexdigest() == fsd_md5

    return fsd_pickle
