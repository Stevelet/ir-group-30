import json
import os
from Levenshtein import distance
from statistics import mean

biography_related_topics = ['396', '397', '403', '770', '1371']

index_root = os.path.join(os.getcwd(), '..', '..', '..', '..', '..', '..', '..', '..', 'media', 'steve', 'PortableSSD', 'index')

topic_file = os.path.join(index_root, 'train_topics_meta.jsonl')
generated_query_file = os.path.join(index_root, 'generated_queries.json')
ranking_output_file = os.path.join(index_root, 'ranking_ids.json')

queries = []

with open(generated_query_file, 'r') as fp:
    for line in fp.readlines():
        di = json.loads(line)

        for query in di['queries']:
            queries.append((di['id'], query))

ranking_dict = {}
with open(topic_file, 'r') as fp:
    topics = json.load(fp)

    keyword_dict = topics['keywords']

    for query_key in keyword_dict.keys():
        if str(topics['id'][query_key]) not in biography_related_topics:
            continue
        else:
            print(topics['id'][query_key])

        query_ranking = {}
        keyword_set = set(keyword_dict[query_key].replace('[\'', '').replace('\']', '').split('\', \''))

        for query in queries:
            index = query[0]
            m = mean([distance(keyword, query) for keyword in keyword_set])

            if index in query_ranking.keys():
                if m < query_ranking[index]:
                    query_ranking[index] = m
            else:
                query_ranking[index] = m
        ranking_dict[query_key] = query_ranking

final_ranking_dict = {}
for query_key in ranking_dict.keys():
    ranking = list(map(lambda t: t[0], sorted([(k, v) for k, v in ranking_dict[query_key].items()], key=lambda t: t[1])[0:100]))
    final_ranking_dict[query_key] = ranking

with open(ranking_output_file, 'w') as fp:
    json.dump(final_ranking_dict, fp)
