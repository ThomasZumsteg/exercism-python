import json

class RestAPI(object):
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == '/users':
            return json.dumps(self.database)

    def post(self, url, payload=None):
        if url == '/add':
            data = json.loads(payload)
            new_user ={
                'name': data['user'],
                'owes': {},
                'owed_by': {},
                'balance': 0} 
            self.database[data['user']] = new_user
            return json.dumps(new_user)
        return '{}'
