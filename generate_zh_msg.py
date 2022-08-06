import pickle
import json

dust514_ids = json.load(open('dust514_ids.json', 'r'))

en_msgs = pickle.load(open('localization_fsd_en-us.pickle', 'rb'))
zh_msgs = pickle.load(open('localization_fsd_zh.pickle', 'rb'))

striped_msg = {k: v[0] for k, v in zh_msgs[1].items() if k in en_msgs[1] and k not in dust514_ids}

json.dump(striped_msg, open('translation-zh_Hans.json', 'w', encoding='utf-8'), ensure_ascii=False, sort_keys=True, indent=0)
