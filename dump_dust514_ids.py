import json

from evetypes import GetTypeIDsByCategory, GetNameID, GetDescriptionID

dust514_type_ids = GetTypeIDsByCategory(350001)
dust514_msg_ids = set()

for type_id in dust514_type_ids:
    dust514_msg_ids.add(GetNameID(type_id))
    dust514_msg_ids.add(GetDescriptionID(type_id))

dust514_msg_ids = sorted(x for x in dust514_msg_ids if x is not None)

json.dump(dust514_msg_ids, open(r'dust514_ids.json', 'w'), indent=0)