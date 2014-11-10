"""A school database"""

class School(object):
    """Stores students and the associated grades"""
    def __init__(self, name):
        """Creates the DB"""
        self.name = name
        self.db = {}

    def add(self, student, level):
        """Adds students to the db"""
        try:
            self.db[level].add(student)
        except KeyError:
            self.db[level] = set((student,))

    def grade(self, level):
        """Returns the students in a grade"""
        try:
            return self.db[level]
        except KeyError:
            return set()

    def sort(self):
        """Returns the whole school in alphabetical order"""
        return_db = {}
        for level, students in self.db.iteritems():
            return_db[level] = tuple(sorted(students))
        return return_db
