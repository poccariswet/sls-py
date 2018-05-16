import json


def get_ld_rawdata_2(event, context):
    data = json.loads(event['body'])

    if 'date' in data:
        date = data['date']
    else:
        return {'statusCode': 422,
                'body': json.dumps({'error_message': ' date is not in body.'})}

    if 'BUMONCode' in data:
         BUMONCode = data['BUMONCode']
    else:
         return {'statusCode': 422,
                'body': json.dumps({'error_message': ' BUMONCode is not in body.'})}

    if 'DPTCode' in data:
        DPTCode = data['DPTCode']
    else:
        return {'statusCode': 422,
                'body': json.dumps({'error_message': ' DPTCode is not in body.'})}

    if 'LINECode' in data:
        LINECode = data['LINECode']
    else:
        return {'statusCode': 422,
                'body': json.dumps({'error_message': ' LINECode is not in body.'})}

    if 'CLASSCode' in data:
       CLASSCode = data['CLASSCode']
    else:
        return {'statusCode': 422,
                'body': json.dumps({'error_message': ' CLASSCode is not in body.'})}

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
            "15": 1,
            "16": date,
            "17": BUMONCode,
            "18": DPTCode,
            "19": LINECode,
            "20": CLASSCode
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
            "15": 1,
            "16": date,
            "17": BUMONCode,
            "18": DPTCode,
            "19": LINECode,
            "20": CLASSCode

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
            "15": 1,
            "16": date,
            "17": BUMONCode,
            "18": DPTCode,
            "19": LINECode,
            "20": CLASSCode
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
