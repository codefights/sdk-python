from codefights.model.IFighter import *
from random import randint

class Boxer(IFighter):

    def __init__(self):
        self._attack1 = Area.NOSE
        self._attack2 = Area.JAW
        self._defence = Area.NOSE

        self._myScoreTotal = 0
        self._opponentScoreTotal = 0
        self._comment = ''

    def make_next_move(self, opponents_last_move=None, my_last_score=None,
                       opponents_last_score=None):

        rez = Move()

        rez.add_attack(self._attack1)
        rez.add_attack(self._attack2)
        rez.set_comment('la la la')

        if opponents_last_move is not None:
            if self._defence in opponents_last_move.get_attacks():
                rez.set_comment('blocked your move to my %s hahaha' %
                                self._defence)
            else:
                self._change_defence()

        self._myScoreTotal += my_last_score
        self._opponentScoreTotal += opponents_last_score

        if self._myScoreTotal < self._opponentScoreTotal:
            rez.set_comment('okay, meat, me is mad now... going berserk')
            rez.add_attack(self._create_random_attack())
        else:
            rez.add_block(self._defence)

        return rez

    def _change_defence(self):
        if self._defence == Area.NOSE:
            self._defence = Area.JAW

        self._defence = Area.NOSE

    @staticmethod
    def _create_random_attack():
        random = randint(0, 10)
        if random >= 5:
            return Area.GROIN
        return Area.BELLY
