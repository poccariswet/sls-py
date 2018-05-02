import json


def hello(event, context):
    # TODO: event['body']をパースして、idをとり、select
    body = {
        "message": "success serverless!!!",
        "input": event['body']
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
