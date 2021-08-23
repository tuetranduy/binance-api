from sqlalchemy.exc import SQLAlchemyError

from app.database import Database
from app.server import app
from core import ClientManager
from models.keys import Keys

db = Database()
client_mgr = ClientManager()


def set_keys(request):
    app.logger.debug('set_keys payload: %s', request.form)

    api_key = request.form['api_key']
    secret_key = request.form['secret_key']

    try:

        keys = Keys(api_key, secret_key)
        db.set_keys(keys)

        # Re-initialize to make sure client object always use latest api&secret key
        app.logger.debug('=== Re-initialize client object ===')
        client_mgr.init_client()

        return {
            'data': "Keys saved successfully"
        }

    except SQLAlchemyError as e:
        return {
                   'message': 'Keys saved unsuccessfully',
                   'stack_trace': str(e),
                   'code': 500
               }, 500


def get_keys():
    try:
        keys = db.get_keys()
        return {
            'data': {
                'api_key': keys.api_key,
                'secret_key': keys.secret_key
            }
        }

    except SQLAlchemyError as e:
        return {
                   'message': 'Get keys unsuccessfully',
                   'stack_trace': str(e),
                   'code': 500
               }, 500
