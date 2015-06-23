from codefights.boilerplate.ProtocolException import ProtocolException
from codefights.boilerplate.server.ServerMode import ServerMode
from codefights.boilerplate.Human import Human
from codefights.boilerplate.Arena import Arena
from codefights.samples.Boxer import Boxer
from codefights.samples.Kickboxer import Kickboxer
from codefights.MyFighter import MyFighter


FIGHT_HUMAN_SWITCH = '--fight-me'
FIGHT_BOT_SWITCH = '--fight-bot'
RUN_ON_SERVER_SWITCH = '--fight-on-server'

USAGE_INSTRUCTIONS = '''
%s\t\t%s
%s %s
%s %s
%s\t%s
''' % (FIGHT_HUMAN_SWITCH, 'runs your bot against you in interactive mode',
       FIGHT_BOT_SWITCH, 'boxer\truns your bot against a built-in boxer bot',
       FIGHT_BOT_SWITCH, ' kickboxer\truns your bot against a built-in '
                         'kickboxer bot\n',
       RUN_ON_SERVER_SWITCH, 'runs your bot in codefights engine environment')

class SDK:

    @staticmethod
    def run(argv):
        del argv[0]

        if SDK.is_fight_human_mode(argv):
            arena = Arena()
            arena.register_fighter(Human(), 'You')
            arena.register_fighter(MyFighter(), 'Your bot')
            arena.stage_fight()

        elif SDK.is_fight_bot_mode(argv):
            arena = Arena()
            arena.register_fighter(MyFighter(), 'Your bot')
            arena.register_fighter(SDK.create_bot(argv), argv[1])
            arena.stage_fight()

        elif SDK.is_run_in_server_mode(argv):
            serverMode = ServerMode()
            serverMode.run(MyFighter())

        else:
            SDK.print_usage_instructions(argv)

    @staticmethod
    def is_run_in_server_mode(args):
        return len(args) == 1\
            and args[0].lower() == RUN_ON_SERVER_SWITCH.lower()

    @staticmethod
    def is_fight_bot_mode(args):
        return len(args) >= 2 \
            and args[0].lower() == FIGHT_BOT_SWITCH.lower()

    @staticmethod
    def is_fight_human_mode(args):
        return len(args) == 1 and args[0].lower() == FIGHT_HUMAN_SWITCH.lower()

    @staticmethod
    def print_usage_instructions(args):
        if len(args) > 0:
            print 'unrecognized option(s): '

            for arg in args:
                print arg + ' '

            print '\n'

        print USAGE_INSTRUCTIONS

    @staticmethod
    def create_bot(args):
        if 'boxer' == args[1]:
            return Boxer()

        if 'kickboxer' == args[1]:
            return Kickboxer()

        raise ProtocolException('unrecognized built-in bot: %s' % args[1])