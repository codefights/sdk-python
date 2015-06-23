import sys
from codefights.boilerplate.server.Protocol import ServerResponse, Protocol


class ServerMode:

    def __init__(self):
        self._in_stream = sys.stdin
        self._out_stream = sys.stdout
        self._cancel_flag = False

    def run(self, fighter):
        protocol = Protocol(self._in_stream, self._out_stream)
        protocol.handshake()

        resp = ServerResponse()

        while not self._cancel_flag:
            move = fighter.make_next_move(resp.move, resp.score1, resp.score2)
            protocol.send_request(move)
            resp = protocol.read_response()

    def set_input_stream(self, istream):
        self._in_stream = istream

    def set_output_stream(self, ostream):
        self._out_stream = ostream

    def cancel(self):
        self._cancel_flag = True
