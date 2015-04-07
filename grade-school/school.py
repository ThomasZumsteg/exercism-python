"""A school database"""
from collections import defaultdict

class School(object):
    """Stores students and the associated grades"""
    def __init__(self, name):
        """Creates the DB"""
        self.name = name
        self.db = defaultdict(set)

    def add(self, student, level):
        """Adds students to the db"""
        self.db[level].add(student)
        
    def grade(self, level):
        """Returns the students in a grade"""
        return self.db[level]

    def sort(self):
        """Returns the whole school in alphabetical order"""
        return {grade: tuple(sorted(students)) 
                for grade, students in self.db.iteritems()}