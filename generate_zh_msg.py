import pickle
import json

en_msgs = json.load(open('translation-en.json', 'r', encoding='utf-8'))
zh_msgs = pickle.load(open('localization_fsd_zh.pickle', 'rb'))

striped_msg = {k: v[0] for k, v in zh_msgs[1].items() if str(k) in en_msgs}

json.dump(striped_msg, open('translation-zh_Hans.json', 'w', encoding='utf-8'), ensure_ascii=False, sort_keys=True, indent=0)
