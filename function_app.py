import logging

import azure.functions as func

app = func.FunctionApp()


@app.route(
    route="webhook",
    methods=["POST"],
    auth_level=func.AuthLevel.FUNCTION
)
def webhook(req: func.HttpRequest) -> func.HttpResponse:

    logging.info("Webhook received")

    return func.HttpResponse(
        "WP Corporate Analytics Webhook Online",
        status_code=200
    )
