import logging
import os

import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.DEBUG
)

sentry_sdk.init(
    dsn="https://8da41b4c0bf242259ce4dc058806508e@o446295.ingest.sentry.io/5882138",
    integrations=[FlaskIntegration(), sentry_logging],
    traces_sample_rate=1.0,
    environment=os.environ['FLASK_ENV'],
)

app = Flask(__name__, instance_relative_config=True)

app.logger.setLevel(logging.INFO)

from app import routes  # type: ignore
