from codefights.model.Area import Area

class GameScoringRules:

    def __init__(self):
        self.NOSE_SCORE = 10
        self.JAW_SCORE = 8
        self.BELLY_SCORE = 6
        self.GROIN_SCORE = 4
        self.LEGS_SCORE = 3

        self.LIFEPOINTS = 150

    def calculate_score(self, attacks, blocks):
        rez = 0

        if attacks:
            for attack in attacks:
                if attack in blocks:
                    continue

                rez += self.get_attack_severity(attack)

        return rez

    def get_attack_severity(self, attack):
        if attack == Area.NOSE:
            return self.NOSE_SCORE

        if attack == Area.JAW:
            return self.JAW_SCORE

        if attack == Area.GROIN:
            return self.GROIN_SCORE

        if attack == Area.BELLY:
            return self.BELLY_SCORE

        if attack == Area.LEGS:
            return self.LEGS_SCORE

        raise Exception('Unknown attack vector: ' + attack)

    @staticmethod
    def is_move_legal(move):
        attacks = move.get_attacks()
        blocks = move.get_blocks()
        return len(attacks) + len(blocks) <= 3
