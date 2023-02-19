from flask import Flask
from datetime import datetime
import pytz

time_zone = "Europe/Moscow"
time = "%d.%m.%Y %H:%M:%S"

app = Flask(__name__)


@app.route("/")
def get_time():
    moscow_time = datetime.now(pytz.timezone(time_zone)).strftime(time)
    return '<h1>' + moscow_time + '</h1>'
