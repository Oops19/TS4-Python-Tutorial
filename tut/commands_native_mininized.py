import os
import traceback
import sims4.commands


def logger(message: str, output):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "log.txt"), "a") as fp:
        fp.write(f'{message}\n')


@sims4.commands.Command('o19.tut.commands.2_min', command_type=sims4.commands.CommandType.Live)
def o19_cheat_tut_commands_two_min(i: int, _connection=None):
    try:
        logger(f"10/{i} = '{10/i:3.2f}'", None)
    except Exception as e:
        logger(f"{traceback.format_exc()}", None)

'''
Down to 12 lines, so it is a long as the S4CL implementation.

Features to be implemented:
* Log file management / rotation.
* Add help messages
'''

