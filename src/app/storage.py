from datetime import datetime, timedelta

class TokenStorage():
    storage = {}

    def addToken(self, id:int, token:str, expires_at:str):
        self.storage[id] = {
            "token": token,
            "expires_at": expires_at 
        }
    
    def isTokenValid(self, id:int):
        token = self.storage.get(id)
        if token is None:
            return False
        current_expiration = datetime.strptime(token.get("expires_at") , '%Y-%m-%dT%H:%M:%SZ')
        current_datetime = datetime.now()

        return current_datetime < (current_expiration - timedelta(minutes=10))

    def getToken(self, id:int):
        return self.storage.get(id)
