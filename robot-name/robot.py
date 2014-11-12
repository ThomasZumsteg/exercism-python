"""Names robots"""
from string import uppercase

class Robot(object):
    """A robot naming class"""
    num_robots = 0

    def __init__(self):
        """Creates a new robot name"""
        self.name = self.create_name()

    def reset(self):
        """Gives the robot a new name"""
        self.name = self.create_name()

    @staticmethod
    def create_name():
        """Changes the number of robots into name"""
        # Creates a binary representation of the number of robots
        robot_num = format(Robot.num_robots % 10**3 * 26**2, "020b")
        # Mangles it
        robot_num = int(robot_num[0::2] + robot_num[1::2], 2)
        # Picks the last three digits
        digit_seed = robot_num % 1000
        chr_seed = (robot_num // 10**3) % 676
        name = "%c%c%03d" %(uppercase[chr_seed // 26 - 1],
                            uppercase[chr_seed % 26], digit_seed)
        Robot.num_robots += 1
        return name
