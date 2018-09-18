import json

class RestAPI(object):
    def __init__(self, database=None):
        self.database = database

    def _select_username(self, username):
        for user in self.database['users']:
            if user['name'] == username:
                return user


    def get(self, url, payload=None):
        data = json.loads(payload) if payload else None
        if url == '/users':
            if payload is None:
                return json.dumps(self.database)
            username = data['users']
            result = { 'users' : 
                [self._select_username(username)] }
        return json.dumps(result)


    def post(self, url, payload=None):
        data = json.loads(payload)
        result = {}
        if url == '/add':
            result = {
                'name': data['user'],
                'owes': {},
                'owed_by': {},
                'balance': 0} 
            self.database[data['user']] = result
        elif url == '/iou':
            borrower = self._select_username(data['borrower'])
            lender = self._select_username(data['lender'])
            amount = data['amount']
            borrower['owes'][lender['name']] = amount
            borrower['balance'] -= amount
            lender['owed_by'][borrower['name']] = amount
            lender['balance'] += amount
            result = { 'users': [lender, borrower]}
        return json.dumps(result)
