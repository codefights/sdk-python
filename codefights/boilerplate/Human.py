from codefights.model.IFighter import *
from codefights.boilerplate.server.Protocol import Protocol
from codefights.boilerplate.ProtocolException import ProtocolException
import sys

class Human(IFighter):

    def __init__(self):
        self._console_out = sys.stdout
        self._console_in = sys.stdin

    def make_next_move(self, opp_move=None, i_scored=0, opp_scored=0):
        self._print_instructions()

        while True:

            try:
                return self._parse_input(self._console_in.readline().strip())
            except ProtocolException, msg:
                print 'Human error: %s' % msg
            except Exception:
                sys.exit('Bye')

    def _print_instructions(self):

        message = '%s %s: ' % ('Make your move by (A)ttacking and (B)locking '
                               '(N)ose, (J)aw, (B)elly, (G)roin, (L)egs',
                               '(for example, BN BB AN)')

        self._console_out.write(message)

    @staticmethod
    def _parse_input(input_):
        input_ = input_.replace(' ', '').lower()

        if Human._starts_with(input_, 'q'):
            raise Exception('Exiting')

        move = Protocol.parse_move(input_)
        if not GameScoringRules.is_move_legal(move):
            raise ProtocolException('Can make max 3 things at a time!')

        return move

    @staticmethod
    def _starts_with(haystack, needle):
        return haystack[0:len(needle)] == needle
