from codefights.boilerplate.ProtocolException import ProtocolException
from codefights.model.Area import Area
from codefights.model.Move import Move
import re

class ServerResponse:

    def __init__(self):
        self.move = None
        self.score1 = None
        self.score2 = None


class Protocol:
    def __init__(self, in_stream, out_stream):
        self.HANDSHAKE = 'I-AM ready'

        self.REQUEST_HEADER = ''

        self.YOUR_SCORE = 'YOUR-SCORE'
        self.OPPONENT_SCORE = 'OPPONENT-SCORE'
        self.ENEMY_MOVE = 'ENEMY-MOVE'
        self.MOVE_COMMENT = 'COMMENT'

        self.in_stream = in_stream
        self.out_stream = out_stream

    def handshake(self):
        self.out_stream.write(self.out_stream,
                              self.HANDSHAKE + '\n')
        self.out_stream.flush()

    def send_request(self, move):
        self.out_stream.write(self.REQUEST_HEADER + self.serialize_move(move))
        self.out_stream.flush()

    def read_response(self):
        return self.parse(self.in_stream.readline())

    @staticmethod
    def serialize_move(self, move):
        rez = ''

        for attack in move.get_attacks():
            rez += 'a' + attack[0]

        for block in move.get_blocks():
            rez += 'b' + block[0]

        if move.get_comment():
            rez += 'c' + self.sanitize_comment(move.get_comment())

        return rez.lower()

    @staticmethod
    def parse_move(input_):
        if not input_:
            raise ProtocolException('Input stream was closed')

        input_ = input_.strip()

        rez = Move()

        index = 0

        while index < len(input_):
            type_ = input_[index]
            index += 1

            if type_ == 'a':
                rez.add_attack(Protocol._get_area(input_, index))
                index += 1

            elif type_ == 'b':
                rez.add_block(Protocol._get_area(input_, index))
                index += 1

            elif type_ == 'c':
                rez.set_comment(input_[index:])
                index += 1

            elif type_ not in ['.', ' ', '\t']:
                raise ProtocolException('Unrecognized input: ' + type_)

        return rez

    @staticmethod
    def sanitize_comment(comment):
        if not comment:
            return None

        breaks = ur'\t|\n|"'
        result = re.sub(breaks, " ", comment).strip()

        if len(comment) > 150:
            result = result[0:150]

        return result

    def parse(self, line):
        result = ServerResponse()

        words = line.split(' ')
        index = 0

        while index < len(words):
            first_keyword = words[index]
            index += 1

            if index >= len(words):
                raise ProtocolException('Insufficient params in {' +
                                        line +
                                        '}. Syntax is [YOUR-SCORE area] '
                                        '[OPPONENT-SCORE area] '
                                        '[ENEMY-MOVE move]')

            next_keyword = words[index]
            index += 1

            if self.YOUR_SCORE.lower() == first_keyword.lower():
                result.score1 = int(next_keyword)
            elif self.OPPONENT_SCORE.lower() == first_keyword.lower():
                result.score2 = int(next_keyword)
            elif self.ENEMY_MOVE.lower() == first_keyword.lower():
                result.move = Protocol.parse_move(next_keyword)
            else:
                raise ProtocolException('invalid keyword ' +
                                        first_keyword +
                                        '. Syntax is [YOUR-SCORE area] '
                                        '[OPPONENT-SCORE area] '
                                        '[ENEMY-MOVE move]')

        return result

    @staticmethod
    def _get_area(line, index):
        if index >= len(line):
            raise ProtocolException('Must also specify attack/defence area!')

        options = {
            'n': Area.NOSE,
            'j': Area.JAW,
            'b': Area.BELLY,
            'g': Area.GROIN,
            'l': Area.LEGS
        }

        if line[index] in options:
            return options[line[index]]
        else:
            raise ProtocolException('Unrecognized area: ' + line[index])
