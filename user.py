import base64
from datetime import datetime, timedelta
import os

class User():
    # ...
    token = ""
    token_expiration = datetime.now() - timedelta(seconds=1)

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