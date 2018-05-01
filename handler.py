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

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
