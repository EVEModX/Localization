import pickle
import json

from generate_en_template import build_template_str



if __name__ == "__main__":
    en_msgs = json.load(open('langs/translation-en.json', 'r', encoding='utf-8'))
    zh_msgs = pickle.load(open('localization_fsd_zh.pickle', 'rb'))

    striped_msg = {str(k): build_template_str(v) for k, v in zh_msgs[1].items() if str(k) in en_msgs}

    json.dump(striped_msg, open('langs/translation-zh_Hans.json', 'w', encoding='utf-8'), ensure_ascii=False, sort_keys=True, indent=0)
