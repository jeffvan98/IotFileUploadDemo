import azure.functions as func
import datetime
import json
import logging

bp = func.Blueprint()

@bp.function_name("journal_storage_message")
@bp.blob_trigger(
    arg_name="inputMessage",
    path="%BlobContainer%/{name}",
    connection="BlobConnection")
@bp.table_output(
    arg_name="outputMessage", 
    connection="TableConnection",
    table_name="%TableName%",
    partition_key="PartitionKey")
def journal_storage_message(inputMessage: func.InputStream, outputMessage: func.Out[str]):
    logging.info("journal_storage_message")

    rowKey = str(datetime.datetime.now())
    message = f"journal_storage_message received '{inputMessage.uri}'"
    data = {
        "PartitionKey": "42",
        "RowKey": rowKey,
        "Source": "journal_storage_message",
        "Message": message
    }

    outputMessage.set(json.dumps(data))
