#!/usr/bin/env python3

import os
from ast import main
import pickle
import json

from download_pickle import download_fsd_pickle

SEPERATOR = "\n!====FORMAT-KWARGS====!\n"

def build_template_str(row):
    if row[2]:
        return row[0] + SEPERATOR + json.dumps(row[2], ensure_ascii=False, sort_keys=True, indent=2)
    else:
        return row[0]

if __name__ == "__main__": 
    dust514_ids = json.load(open('dust514_ids.json', 'r'))
    
    en_msgs = pickle.loads(download_fsd_pickle())

    striped_msg = {k: build_template_str(v) for k, v in en_msgs[1].items() if k not in dust514_ids and v[0].strip()}

    os.makedirs('langs/', exist_ok=True)
    json.dump(striped_msg, open('langs/translation-en.json', 'w', encoding='utf-8'), ensure_ascii=False, sort_keys=True, indent=0)