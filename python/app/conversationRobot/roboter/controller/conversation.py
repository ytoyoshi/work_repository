"""Controller for speaking with robot."""
from roboter.models import robot

def talking():
    """Function to speak with Robot"""
    talking_robot = robot.Robot()
    talking_robot.hello()
    print('###')
    talking_robot.goodbye()
    print('###')
    