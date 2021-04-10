#!/usr/bin/env python3
"""User model"""
from sqlalchemy import create_engine, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:

    def __init__(self):
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """save the user to the database"""
        new = User(email=email, hashed_password=hashed_password)
        self._session.add(new)
        self._session.commit()
        return new

    def find_user_by(self, **kwargs) -> User:
        """ first row found in the users table """
        if not kwargs:
            raise InvalidRequestError

        col = User.__table__.columns._data.keys()
        for key in kwargs.keys():
            if key in col:
                new = self._session.query(User).filter_by(**kwargs).first()
                if new is None:
                    raise NoResultFound
                return new
        raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs) -> None:
        """update user found"""
        cols = User.__table__.columns._data.keys()
        for key in kwargs.keys():
            if key not in cols:
                raise ValueError

        session = (update(User)
                   .where(User.id == user_id)
                   .values(**kwargs))
        self._session.execute(session)
        self._session.commit()
