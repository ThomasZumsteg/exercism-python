"""Tracks student plants in a kidnergarden garden"""

class Garden(object):
    """Rembers which student has which plant"""
    # Default student list
    students = ["Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"
               ]

    # Default plant codes
    plant_codes = {"G": "Grass",
                   "C": "Clover",
                   "R": "Radishes",
                   "V": "Violets",
                  }

    # Default number of cups student has per row
    cups_per_row = 2

    def __init__(self, garden, students=None):
        """Builds the student garden"""
        if students:
            self.students = sorted(students)
        # Data structure that holds the garden (dictionary of lists)
        self.student_garden = {}

        # Formats the garden string into rows with groups of cups
        garden = garden.split("\n")
        for i, row in enumerate(garden):
            garden[i] = [row[j:j+self.cups_per_row] \
                         for j in range(0, len(row), self.cups_per_row)]

        # Assigns columns of cups to students
        for student, plants in zip(self.students, zip(*garden)):
            self.student_garden[student] = ''.join(plants)

    def plants(self, student):
        """Translats the string into plant names and returns"""
        return [self.plant_codes[p] for p in self.student_garden[student]]
