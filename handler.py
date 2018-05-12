import json


def hello(event, context):
    # TODO: event['body']をパースして、idをとり、select
    body = event['body']
    Items = []
    Item1 = {
        "Item": {
            "skucode": "0001001",
            "p_name": "コーヒー",
            "9": 4,
            "10": 21,
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
            "p_name": "カフェラテ",
            "9": 4,
            "10": 1,
            "11": 7,
            "12": 9,
            "13": 8,
            "14": 4,
            "15": 1
        }
    }
    Item3 = {
        "Item": {
            "skucode": "0001003",
            "p_name": "お茶",
            "9": 4,
            "10": 1,
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
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Credentials" : True
        },
        "body": json.dumps(Items)
    }

    return response
