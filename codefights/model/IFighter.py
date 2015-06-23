import abc
from codefights.model.Area import Area
from codefights.model.Move import Move
from codefights.model.GameScoringRules import GameScoringRules

class IFighter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def make_next_move(self,
                       opponents_last_move,
                       my_last_score,
                       opponents_last_score):
        raise NotImplementedError
