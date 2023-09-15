import azure.functions as func
import datetime
import json
import logging

bp = func.Blueprint()

@bp.function_name("journal_event_grid_message")
@bp.event_grid_trigger(
    arg_name="inputMessage")
@bp.table_output(
    arg_name="outputMessage", 
    connection="TableConnection",
    table_name="%TableName%",
    partition_key="PartitionKey")
def journal_event_grid_message(inputMessage: func.EventGridEvent, outputMessage: func.Out[str]):
    logging.info("journal_event_grid_message")

    rowKey = str(datetime.datetime.now())
    message = f"journal_event_grid_message received id='{inputMessage.id}'; topic='{inputMessage.topic}'; subject='{inputMessage.topic}'; event_type='{inputMessage.event_type}'; data='{inputMessage.get_json()}';"
    data = {
        "PartitionKey": "42",
        "RowKey": rowKey,
        "Source": "journal_event_grid_message",
        "Message": message
    }

    outputMessage.set(json.dumps(data))
