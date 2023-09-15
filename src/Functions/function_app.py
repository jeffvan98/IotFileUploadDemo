import azure.functions as func
from journal_event_grid_message import bp as grid_bp
from journal_iot_message import bp as iot_bp
from journal_storage_message import bp as storage_bp

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
app.register_functions(grid_bp)
app.register_functions(iot_bp)
app.register_functions(storage_bp)
