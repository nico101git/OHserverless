import logging

import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    productId = req.params.get('productId')
    if not productId:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            productId = req_body.get('productId')

    if productId:
        res={}
        res["data"]=productId
        return func.HttpResponse(json.dumps(res),
        status_code=200, mimetype="application/json")
    else:
        res={}
        res["error"]="This HTTP triggered function executed successfully. Pass a productId in the query string or in the request body for a personalized response."
        return func.HttpResponse(
             json.dumps(res),
             status_code=400,
             mimetype="application/json"
        )
