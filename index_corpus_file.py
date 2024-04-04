import os
import json

download_root = os.path.join(os.getcwd(), '..', '..', '..', 'mnt', 'g', 'TRECCorpus')
corpus_file_location = os.path.join(download_root, 'trec_corpus_20220301_plain.json')
query_file_location = os.path.join(os.getcwd(), 'train_topics_meta.jsonl')
meta_file_location = os.path.join(download_root, 'trec_2022_articles_discrete_V2.json')

index_root = os.path.join(os.getcwd(), '..', '..', '..', 'mnt', 'k')
index_location = os.path.join(index_root, 'index')
meta_index_location = os.path.join(index_location, 'meta_index.json')
augmented_index_location = os.path.join(index_location, 'augmented_index.json')

meta_map = {}
gender_set = {"Man", "Woman", "Non-binary"}

check_id = 12148915

if not os.path.exists(meta_index_location):
    with open(meta_file_location, 'r') as f:
        for line in f:
            di = json.loads(line)
            if di['gender_category'] in gender_set:
                meta_map[str(di["page_id"])] = {
                    'pred_qual': di['pred_qual'],
                    'qual_cat': di['qual_cat'],
                    'page_countries': di['page_countries'],
                    'page_subcont_regions': di['page_subcont_regions'],
                    'gender': di['gender'],
                    'gender_category': di['gender_category'],
                    'occupations': di['occupations']
                }
    with open(meta_index_location, 'w') as f:
        json.dump(meta_map, f)
else:
    with open(meta_index_location, 'r') as f:
        meta_map = json.load(f)

with open(corpus_file_location,'r',buffering=100000) as f:
    for line in f:
        di = json.loads(line)

        if str(di['id']) in meta_map.keys():
            augmented_dict = meta_map[str(di['id'])]
            augmented_dict.update(di)
            js_str = json.dumps(augmented_dict) + '\n'
            with open(augmented_index_location, 'a') as f1:
                f1.write(js_str)
print("Done")