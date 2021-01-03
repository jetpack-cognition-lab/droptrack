import os
from typing import Optional, Union
from flask import current_app
from dataclasses import dataclass


users = [
    {
        'id': 1,
        'name': 'x',
        'api_token': 'yuOJX-8paOqRJR8iefr7vL-Ozu5owbSUtr8SIM0K1L1EKPB9mWjPM52nydMEFyl7',
    }
]


class Token:

    __token: str

    def __init__(self, token):
        assert len(token) == 64
        self.__token = token

    def __str__(self):
        return self.__token

    def __eq__(self, other: Union[str, 'Token']):
        return str(self) == other


@dataclass
class User:

    id: int
    name: str
    api_token: Token

    @staticmethod
    def verify_api_token(token: str) -> Optional['User']:
        if token:
            for user in users:
                if user['api_token'] == token:
                    return User(**user)
        return None

    @property
    def home_directory(self):
        return os.path.join(current_app.config['UPLOAD_DIR'], self.name)
