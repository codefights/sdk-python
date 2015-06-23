from codefights.boilerplate.ProtocolException import ProtocolException
from codefights.boilerplate.Commentator import Commentator
from codefights.model.GameScoringRules import GameScoringRules


class Arena:

    def __init__(self):
        self._fighters = []
        self._commentator = Commentator()

    def register_fighter(self, fighter, name):
        self._fighters.append({
            'name': name,
            'fighter': fighter
        })
        return self

    def stage_fight(self):
        if len(self._fighters) != 2:
            raise ProtocolException('Must be 2 fighters!')

        f2 = self._fighters.pop()
        f1 = self._fighters.pop()

        f1name = f1['name']
        fighter1 = f1['fighter']

        f2name = f2['name']
        fighter2 = f2['fighter']

        self._commentator.set_fighter_names(f1name, f2name)

        f1_move = None
        f2_move = None

        score1 = 0
        score2 = 0

        f1_lifepoints = GameScoringRules().LIFEPOINTS
        f2_lifepoints = GameScoringRules().LIFEPOINTS

        while f1_lifepoints > 0 and f2_lifepoints > 0:
            move1 = fighter1.make_next_move(f2_move, score1, score2)
            if not GameScoringRules.is_move_legal(move1):
                raise ValueError('%s made an illegal move: %s' % (f1name,
                                                                  move1))

            move2 = fighter2.make_next_move(f1_move, score2, score1)
            if not GameScoringRules.is_move_legal(move2):
                raise ValueError('%s made an illegal move: %s' % (f2name,
                                                                  move2))

            score1 = GameScoringRules().calculate_score(move1.get_attacks(),
                                                       move2.get_blocks())
            score2 = GameScoringRules().calculate_score(move2.get_attacks(),
                                                       move1.get_blocks())

            self._commentator.describe_round(move1, move2, score1, score2)

            f1_lifepoints -= score2
            f2_lifepoints -= score1

            f1_move = move1
            f2_move = move2

        self._commentator.game_over(f1_lifepoints, f2_lifepoints)

    def set_commentator(self, c):
        self._commentator = c
        return self
