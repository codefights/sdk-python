class Move():
    def __init__(self):
        self.attacks = []
        self.blocks = []
        self.comment = ''

    def get_attacks(self):
        return self.attacks

    def get_blocks(self):
        return self.blocks

    def get_comment(self):
        return self.comment

    def add_attack(self, area):
        self.attacks.append(area)
        return self

    def add_block(self, area):
        self.blocks.append(area)
        return self

    def set_comment(self, comment):
        self.comment = comment
        return self

    def __str__(self):
        rez = 'Move '

        for attack in self.attacks:
            rez += ' ATTACK ' + attack

        for block in self.blocks:
            rez += ' BLOCK ' + block

        if self.comment:
            rez += ' COMMENT ' + self.comment

        return rez

    def __repr__(self):
        return self.__str__()
