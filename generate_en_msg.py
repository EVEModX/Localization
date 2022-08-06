import pickle
import json

dust514_ids = json.load(open('dust514_ids.json', 'r'))

en_msgs = pickle.load(open('localization_fsd_en-us.pickle', 'rb'))

striped_msg = {k: v[0] for k, v in en_msgs[1].items() if k not in dust514_ids and v[0].strip()}

json.dump(striped_msg, open('translation-en.json', 'w', encoding='utf-8'), ensure_ascii=False, sort_keys=True, indent=0)