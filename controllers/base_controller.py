from app.database import Database
from core import ClientManager


class BaseController:
    client = None
    database = None
    keys = None

    def __init__(self):
        self.client = ClientManager().init_client()
        self.database = Database()
        self.get_keys()

    def re_initialize_client(self):
        self.client = None
        self.client = ClientManager().init_client()

    def get_keys(self):
        self.keys = self.database.get_keys()
