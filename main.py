from robotics.concrete.command import RoboticsCommandFactory
from robotics.framework.action import CSVAction, Action
from robotics.concrete.robot import RoboticsRobot


def getActionFromName(name: str) -> Action:
    return CSVAction('actions/{name}.csv'.format(name=name), RoboticsCommandFactory())


if __name__ == '__main__':
    bot = RoboticsRobot('COM1')
    bot.doAction(getActionFromName("car"))
    bot.close()
