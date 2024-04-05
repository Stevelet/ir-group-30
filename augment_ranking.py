import os
import json

index_root = os.path.join(os.getcwd(), '..', '..', '..', '..', '..', '..', '..', '..', 'media', 'steve', 'PortableSSD', 'index')

ranking_file = os.path.join(index_root, 'ranking_ids.json')
augmented_ranking_ids = os.path.join(index_root, 'augmented_ranking_index.json')
final_ranking = os.path.join(index_root, 'llm_ranking.json')

with open(augmented_ranking_ids, 'r') as fp:
    ranking_ids = json.load(fp)

with open(ranking_file, 'r') as fp:
    ranking = json.load(fp)



filled_ranking_dict = {}
for key in ranking:
    filled_ranking = [(index, ranking_ids[str(doc_id)]) for index, doc_id in enumerate(ranking[key])]
    print(filled_ranking)
    filled_ranking_dict[key] = filled_ranking

with open(final_ranking, 'w') as fp:
    json.dump(filled_ranking_dict, fp)