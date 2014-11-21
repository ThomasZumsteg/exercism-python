"""Identifies and cleans up phone numbers"""


class Phone(object):
    """Idenifies and cleans up phone number"""
    def __init__(self, phone_number):
        """Identifies a phone number"""
        self.number = self.clean(phone_number)

    def area_code(self):
        """Returns the phone numbers area code"""
        return self.number[:3]

    def pretty(self):
        """Standard phone number form"""
        return "(%s) %s-%s" %(self.number[:3],
                              self.number[3:6],
                              self.number[6:])

    @staticmethod
    def clean(number):
        """Tries to identify a phone number"""
        digits = [c for c in number if c.isdigit()]
        if len(digits) == 11 and digits[0] == "1":
            return ''.join(digits[1:])
        elif len(digits) != 10:
            return "0000000000"
        else:
            return ''.join(digits)
