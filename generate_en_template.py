#!/usr/bin/env python3

import os
from ast import main
import pickle
import json

from download_pickle import download_fsd_pickle

if __name__ == "__main__": 
    dust514_ids = json.load(open('dust514_ids.json', 'r'))
    
    fsd = download_fsd_pickle()
    en_msgs = pickle.loads(fsd)

    striped_msg = {str(k): v[0] for k, v in en_msgs[1].items() if k not in dust514_ids and v[0].strip()}

    os.makedirs('langs/', exist_ok=True)
    json.dump(striped_msg, open('langs/translation-en.json', 'w', encoding='utf-8'), ensure_ascii=False, sort_keys=True, indent=0)