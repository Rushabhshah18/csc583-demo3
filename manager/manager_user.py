from sqlalchemy.exc import IntegrityError, InvalidRequestError

from manager.manager_database import DatabaseManager
from models.model_user import User


class UserManager(object):
    _SESSION = None

    def __init__(self):
        dbmanager = DatabaseManager()
        self._SESSSION = dbmanager.fetch_session()

    def create_user(self, **kwargs):
        """
        Method to create user
        :param kwargs:
        :return:
        """
        user = User(username=kwargs.get('usr'), password=kwargs.get('pwd'))
        try:
            self._SESSSION.add(user)
            self._SESSSION.commit()
            print("User saved in database.\n")
        except IntegrityError:
            print("Username already exist! Please try again.\n")
            self._SESSSION.rollback()
        except InvalidRequestError:
            self._SESSSION.rollback()

    def fetch_last_user(self):
        """
        Method to fetch last saved user
        :return:
        """
        return self._SESSSION.query(User).order_by(User.id.desc()).first()

    def fetch_all_users(self):
        """
        Method to fetch all user in DB
        :return:
        """
        return self._SESSSION.query(User).all()
