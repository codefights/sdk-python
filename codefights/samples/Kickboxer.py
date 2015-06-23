from codefights.model.IFighter import *
from random import randint

class Kickboxer(IFighter):

    def __init__(self):
        self._attack1 = Area.GROIN
        self._attack2 = Area.NOSE
        self._defence = Area.NOSE

        self.__opponentName = ""
        self._comment = ""

    def make_next_move(self, opponents_last_move, i_lost=None, i_scored=None):

        if opponents_last_move is not None:
            if self._defence in opponents_last_move.get_attacks():
                self._comment = 'ouch'

        self._attack2 = self._create_random_area()

        if opponents_last_move is not None:
            if self._attack1 in opponents_last_move.get_blocks():
                self._attack1 = self._create_random_area()

        move = Move()

        move.add_attack(self._attack1)
        move.add_attack(self._attack2)
        move.add_block(self._defence)
        move.set_comment(self._comment)

        return move
    
    @staticmethod
    def _create_random_area():
        random = randint(0, 100)

        if random < 30:
            return Area.NOSE

        if random < 70:
            return Area.JAW

        if random < 90:
            return Area.GROIN

        return Area.LEGS