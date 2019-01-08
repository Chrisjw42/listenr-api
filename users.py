import base64
from datetime import datetime, timedelta
import os

active_users = []

def is_token_valid(token):
    for i in active_users:
        if i.token == token:
            return True
    return False

class User():
    id = ""
    token = ""
    token_expiration = datetime.now() - timedelta(seconds=1)

    def __init__(self):
        # Initialise a user with a unique ID
        self.id = base64.b64encode(os.urandom(24)).decode('utf-8')

    def get_token(self, expires_in=86400):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        
        # Generate a new token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

#     @staticmethod
    def check_token(self, token):
#         user = User.query.filter_by(token=token).first()
        if token != self.token or self.token_expiration < datetime.utcnow():
            return None
        return self