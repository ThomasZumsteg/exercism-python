from threading import Lock

class BankAccount(object):
    def with_lock(lock):
        def wrapper(func):
            def wrapped(self, *args):
                with getattr(self, lock):
                    return func(self, *args)
            return wrapped
        return wrapper

    def is_open(func):
        def wrapped(self, *args):
            if self._state is not 'opened':
                raise ValueError("Account is {}, not open".format(self._state))
            return func(self, *args)
        return wrapped

    def __init__(self):
        self._balance = 0
        self._state = 'created'
        self._lock = Lock()

    @is_open
    def get_balance(self):
        return self._balance

    def open(self):
        self._state = 'opened'

    @is_open
    @with_lock('_lock')
    def deposit(self, amount):
        if not (0 <= amount):
            raise ValueError("Cannot deposite amount {}".format(amount))
        self._balance += amount

    @is_open
    @with_lock('_lock')
    def withdraw(self, amount):
        if not (0 <= amount <= self._balance):
            raise ValueError("Cannot withdraw amount {}".format(amount))
        self._balance -= amount

    @is_open
    @with_lock('_lock')
    def close(self):
        self._state = 'closed'
        return self._balance
