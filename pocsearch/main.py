from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['http://192.168.31.22:9200/'],
    # http_auth=(username, password)
)
index_name = "aigc"


def PocSearch(question, detail=False, size=5):
    search_query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"category": "vul"}},
                    {"match": {
                        "text": {
                            "query": question,
                            "analyzer": "ik_max_word",
                        }
                    }}
                ]
            }
        },
        "size": size
    }
    result = es.search(index=index_name, body=search_query)
    data = []
    for item in result["hits"]["hits"]:
        data.append({
            "text": item["_source"]["text"] if detail else item["_source"]["text"][:100],
        })
    return data


if __name__ == '__main__':
    import argparse
    import json

    parser = argparse.ArgumentParser()
    parser.add_argument("--question", type=str, default="")
    parser.add_argument("--detail", type=bool, default=False)
    parser.add_argument("--size", type=int, default=5)
    args = parser.parse_args()

    output = {
        "plugin_result": {
            "exit_code": 0,
            "biz": {
            }
        },
        "ver": 1
    }
    items = []
    for item in PocSearch(args.question, args.detail, args.size):
        items.append(item["text"])
    output["plugin_result"]["biz"]["output"] = "\n".join(items)
    print(json.dumps(output))
