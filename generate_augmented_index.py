import json
import os

index_root = os.path.join(os.getcwd(), '..', '..', '..', '..', '..', '..', '..', '..', 'media', 'steve', 'PortableSSD', 'index')

ranking_file = os.path.join(index_root, 'ranking_ids.json')
meta_index_file = os.path.join(index_root, 'meta_index.json')
augmented_ranking_ids = os.path.join(index_root, 'augmented_ranking_index.json')

ranking_ids = {}

with open(ranking_file, 'r') as fp:
    d = json.load(fp)
    for key in d.keys():
        ranking = d[key]

        for i in ranking:
            ranking_ids[str(i)] = {}

with open(meta_index_file,'r',buffering=1000) as f:
    stop = False
    for line in f.readlines():
        if stop:
            break
        d = json.loads(line)

        for i in d.keys():
            if str(i) in ranking_ids.keys():
                ranking_ids[str(i)] = {
                    'gender_category': d[i]['gender_category'],
                    'qrel': d[i]['pred_qual']
                }

with open(augmented_ranking_ids, 'w') as fp:
    json.dump(ranking_ids, fp)