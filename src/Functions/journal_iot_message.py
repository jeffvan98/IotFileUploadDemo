import azure.functions as func
import datetime
import logging
import json

bp = func.Blueprint()

@bp.function_name("journal_iot_message")
@bp.event_hub_message_trigger(
    arg_name="inputMessage",     
    connection="HubConnection",
    event_hub_name="%HubName%")
@bp.table_output(
    arg_name="outputMessage", 
    connection="TableConnection",
    table_name="%TableName%",
    partition_key="PartitionKey")
def journal_iot_message(inputMessage: func.EventHubEvent, outputMessage: func.Out[str]):
    logging.info("journal_iot_message called")

    rowKey = str(datetime.datetime.now())
    message = f"journal_iot_message received '{inputMessage.sequence_number}'"
    data = {
        "PartitionKey": "42",
        "RowKey": rowKey,
        "Source": "journal_iot_message",
        "Message": message
    }

    outputMessage.set(json.dumps(data))