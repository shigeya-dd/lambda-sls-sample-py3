import json
from ddtrace import tracer
from datadog_lambda.metric import lambda_metric

def hello(event, context):
    lambda_metric(
        "coffee_house.order_value",  # metric name
        12.45,  # metric value
        tags=['product:latte', 'order:online']  # tags
    )

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        # "body": json.dumps(body)
        "body": get_message()
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

@tracer.wrap()
def get_message():
    return "Hello from serverless!"

