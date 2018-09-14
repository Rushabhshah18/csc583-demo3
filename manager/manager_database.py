from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import *

from manager.manager_utils import Singleton


class DatabaseManager(object):
    __metaclass__ = Singleton
    _ENGINE = None
    _SESSION = None

    def __init__(self):
        print("Establishing connection to database...\n")
        # Create session first
        db = DATABASES['default']
        self._ENGINE = create_engine(
            'mysql+mysqldb://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(NAME=db.get('NAME'), USER=db.get('USER'),
                                                                            PASSWORD=db.get('PASSWORD'),
                                                                            HOST=db.get('HOST'), PORT=db.get('PORT')))

        session = sessionmaker(bind=self.fetch_engine())
        self._SESSION = session()

    def fetch_engine(self):
        """
        Method to return db engine
        :return:
        """
        return self._ENGINE

    def fetch_session(self):
        """
        Method to fetch current db session
        :return:
        """
        return self._SESSION
