import json

class RestAPI(object):
    def __init__(self, database=None):
        self.database = database

    def _select_username(self, username):
        for user in self.database['users']:
            if user['name'] == username:
                return user
    
    def lend(self, borrower_name, lender_name, amount):
        borrower = self._select_username(borrower_name)
        lender = self._select_username(lender_name)
        borrower['owes'][lender['name']] = amount
        borrower['balance'] -= amount
        lender['owed_by'][borrower['name']] = amount
        lender['balance'] += amount
        return { 'users': sorted([lender, borrower], key=lambda v: v['name'])}

    def get(self, url, payload=None):
        data = json.loads(payload) if payload else None
        if url == '/users':
            if payload is None:
                result = self.database
            else:
                result = { 'users' : 
                    [self._select_username(data['users'])] }
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
            result = self.lend(data['borrower'], data['lender'], data['amount'])
        return json.dumps(result)
