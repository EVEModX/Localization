#!/usr/bin/env python2

import json
import cPickle as pickle

SEPERATOR = "\n!====FORMAT-KWARGS====!\n"

def convert_types(param):
    converted = {}
    for ph_key, ph_param in param.iteritems():
        ph_converted = {}
        for k, v in ph_param.iteritems():
            if k == u'kwargs':
                kwargs_coverted = {}
                for kwargs_k, kwargs_v in v.iteritems():
                    if kwargs_k in ('from', 'to', 'linkinfo', 'quantity'):
                        kwargs_coverted[str(kwargs_k)] = str(kwargs_v) if isinstance(kwargs_v, unicode) else kwargs_v
                    else:
                        kwargs_coverted[str(kwargs_k)] = kwargs_v
                ph_converted[str(k)] = kwargs_coverted
            elif k in (u'variableName', u'propertyName'):
                ph_converted[str(k)] = str(v) if isinstance(v, unicode) else v
            else:
                ph_converted[str(k)] = v
        converted[ph_key] = ph_converted
    return converted

if __name__ == "__main__": 
    zh_msgs = json.load(open('langs/translation-zh_Hans.json', 'r'))
    zh_fsd = {}
    for k, v in zh_msgs.iteritems():
        if v != "!DNT":
            if SEPERATOR in v:
                splited = v.split(SEPERATOR)
                if len(splited) != 2:
                    raise ValueError(k)
                tmpl = splited[0]
                param = convert_types(json.loads(splited[1]))
                zh_fsd[int(k)] = (tmpl, None, param)
            else:
                zh_fsd[int(k)] = (v, None, None)
                
    zh_fsd = ('zh', zh_fsd)
    pickle.dump(zh_fsd, open('localization_fsd_zh.pickle', 'wb'), protocol=2)
