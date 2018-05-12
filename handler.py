import json


def hello(event, context):
    # TODO: event['body']をパースして、idをとり、select
    body = event['body']
    Items = []
    Item1 = {
        "Item": {
            "skucode": "0001002",
            "商品名": "コーヒー",
            "9": 4,
            "11": 7,
            "12": 9,
            "13": 8,
            "14": 4,
            "15": 1
        }
    }
    Item2 = {
        "Item": {
            "skucode": "0001002",
            "商品名": "コーヒー",
            "9": 4,
            "11": 7,
            "12": 9,
            "13": 8,
            "14": 4,
            "15": 1
        }
    }
    Item3 = {
        "Item": {
            "skucode": "0001002",
            "商品名": "コーヒー",
            "9": 4,
            "11": 7,
            "12": 9,
            "13": 8,
            "14": 4,
            "15": 1
        }
    }
    Items = [Item1, Item2, Item3]

    response = {
        "statusCode": 200,
        "body": json.dumps(Items)
    }

    return response
