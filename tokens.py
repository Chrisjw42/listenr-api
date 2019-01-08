import base64
from datetime import datetime, timedelta
import os

def get_token(self, expires_in=86400):
    now = datetime.utcnow()
    if self.token and self.token_expiration > now + timedelta(seconds=60):
        return self.token
    
    # Generate a new token
    self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
    self.token_expiration = now + timedelta(seconds=expires_in)
    return self.token

def revoke_token():
    pass
    