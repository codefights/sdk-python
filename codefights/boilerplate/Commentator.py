from codefights.model.GameScoringRules import GameScoringRules
from codefights.boilerplate.server.Protocol import Protocol

class Commentator:

    def __init__(self):
        self._fighter1 = 'Fighter1'
        self._fighter2 = 'Fighter2'

        self._lp1 = GameScoringRules().LIFEPOINTS
        self._lp2 = GameScoringRules().LIFEPOINTS

    def set_fighter_names(self, fighter1name, fighter2name):
        self._fighter1 = fighter1name
        self._fighter2 = fighter2name

    def describe_round(self, move1, move2, score1, score2):
        self._describe_move(self._fighter1, move1, score1, move2)
        self._describe_move(self._fighter2, move2, score2, move1)

        self._lp1 -= score2
        self._lp2 -= score1

        print '%s vs %s: %s to %s' % (
            self._fighter1,
            self._fighter2,
            self._lp1,
            self._lp2
        )

    def game_over(self, f1_lifepoints, f2_lifepoints):
        print 'FIGHT OVER'

        if f1_lifepoints > f2_lifepoints:
            print 'THE WINNER IS %s' % self._fighter1

        elif f2_lifepoints > f1_lifepoints:
            print 'THE WINNER IS %s' % self._fighter2

        else:
            print 'IT\'S A DRAW!!!'

    @staticmethod
    def _describe_move(fighter_name, move, score, counter_move):
        print '%s%s%s%s' % (
            fighter_name,
            Commentator._describe_attacks(move, counter_move, score),
            Commentator._describe_defences(move),
            Commentator._describe_comment(move)
        )

    @staticmethod
    def _describe_attacks(move, counter_move, score):
        attacks = move.get_attacks()

        if len(attacks) <= 0:
            return ' did not attack at all '

        rez = ' attacked '

        for attack in attacks:
            rez += attack

            blocked = attack in counter_move.get_blocks()

            if blocked:
                rez += '(-), '
            else:
                rez += '(+), '

        return '%s %s %s' % (rez, 'scoring', score)

    @staticmethod
    def _describe_defences(move):
        blocks = move.get_blocks()

        if len(blocks) <= 0:
            return ' and was not defending at all.'

        rez = ' while defending '
        for block in blocks:
            rez += block + ', '

        return rez

    @staticmethod
    def _describe_comment(move):
        comment = move.get_comment()

        if not comment or comment is None or len(comment) <= 0:
            return ''

        return ' Also said "%s"' % Protocol.sanitize_comment(comment)
