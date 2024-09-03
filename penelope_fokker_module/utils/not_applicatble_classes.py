from typing import Union


class NotYetComputed:
    def __repr__(self):
        return self.__class__.__name__


class NoRobotModelSpecified:
    def __repr__(self):
        return self.__class__.__name__


class NoEndEffectorSpecified:
    def __repr__(self):
        return self.__class__.__name__

    @staticmethod
    def get_compatible_operations():
        return []


class NoForceComputationModelSpecified:
    def __repr__(self):
        return self.__class__.__name__


class NoRobotComputationModel:
    def __repr__(self):
        return self.__class__.__name__


class NotYetImplemented:
    def __repr__(self):
        return self.__class__.__name__


class NoTaskAllocated:
    def __repr__(self):
        return self.__class__.__name__


class NoTaskFound:
    def __repr__(self):
        return self.__class__.__name__


class NoObstacleForces:
    def __repr__(self):
        return self.__class__.__name__


class ZeroForce:
    def __repr__(self):
        return self.__class__.__name__


class NoFeedbackReceived(Exception):
    """Raised if the program has not received any feedback when it is expected."""

    def __init__(self, message: Union[str, int]):
        message = "No feedback was received for message: {0}.".format(message)
        super().__init__(message)


class NotApplicable:
    def __repr__(self):
        return self.__class__.__name__
