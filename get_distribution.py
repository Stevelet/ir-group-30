import json
import os

index_root = os.path.join(os.getcwd(), '..', '..', '..', '..', '..', '..', '..', '..', 'media', 'steve', 'PortableSSD', 'index')

distribution_file = os.path.join(index_root, 'distribution.json')
meta_index_file = os.path.join(index_root, 'meta_index.json')

distribution = {}

with open(meta_index_file,'r',buffering=1000) as f:
    stop = False
    for line in f.readlines():
        if stop:
            break
        d = json.loads(line)

        for i in d.keys():
            distribution.setdefault(d[i]['gender_category'], 0)
            distribution[d[i]['gender_category']] = distribution[d[i]['gender_category']] + 1

with open(distribution_file, 'w') as fp:
    json.dump(distribution, fp)
