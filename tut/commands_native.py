"""
Save this file in 'The Sims 4/Mods/_o19_/tut/' as 'commands_native.py'
Enable custom content and script mods
"""

# Import of native python classes
import os
import traceback

# Import of TS4 classes
import sims4
import sims4.commands

'''
The @ decorator refers to this class:
core.sims4.commands.Command(*aliases, command_type=CommandType.DebugOnly, command_restrictions=CommandRestrictionFlags.UNRESTRICTED, pack=None, console_type=None)
We can use it to register our own commands.
'''

@sims4.commands.Command('o19.tut.commands.0', command_type=sims4.commands.CommandType.Live)
def o19_cheat_tut_commands_zero(i: int, _connection=None):
    """
    :param i: A required parameter. Without a parameter this command will not work. With a string parameter our method will not be called.
    Valid values: '11', '0x11' (will be converted properly)
    Invalid values: '010', 'abc'
    :param _connection: to retrieve a pipe to the console
    :return:
    """
    output = sims4.commands.CheatOutput(_connection)  # Get a pipe to write to the console.
    output(f"10/{i} = '{10/i}'")  # Writing 10/i to the console. If something goes wrong the method ends here without further information
    output(f"10/{i} = '{10/i:.2f}'")  # Making use of a format string to show only two digits
    output(f'OK')


@sims4.commands.Command('o19.tut.commands.1', command_type=sims4.commands.CommandType.Live)
def o19_cheat_tut_commands_one(i: int, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    try:  # try/except block to catch errors
        output(f"10/{i} = '{10/i:3.2f}'")
        output(f'OK')
    except Exception as e:  # catch an exception, most likely the user entered '0'
        logger(f"Oops: {e}", output)
        logger(f"{traceback.format_exc()}", output)


def logger(message: str, output):
    """
    :param message: The message to log
    :param output: A pipe to write to the console. Writing large amount of data to the console takes very long!
    :return:
    """
    if output:
        output(f"{message}")
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "log.txt")
    with open(filename, "a") as fp:
        fp.write(f'{message}\n')


@sims4.commands.Command('o19.tut.commands.2', command_type=sims4.commands.CommandType.Live)
def o19_cheat_tut_commands_two(i: int, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    try:
        logger(f"10/{i} = '{10/i:3.2f}'", output)  # We start logging our data to a file
    except Exception as e:
        logger(f"Oops: {e}", output)
        logger(f"{traceback.format_exc()}", output)


@sims4.commands.Command('o19.tut.commands.3', command_type=sims4.commands.CommandType.Live)
def o19_cheat_tut_commands_three(i: int = 10, _connection=None):  # 10 as the default value for i
    """
    :param i: An optional parameter. Without a parameter the value 10 will be used. String parameters will not call this method.
    """
    output = sims4.commands.CheatOutput(_connection)
    try:
        logger(f"{10/i:.2f}", output)
    except Exception as e:
        logger(f"Oops: {e}", output)
        logger(f"{traceback.format_exc()}", output)


@sims4.commands.Command('o19.tut.commands.4', command_type=sims4.commands.CommandType.Live)
def o19_cheat_tut_commands_four(j: str = '10', _connection=None):  # '10' as the default value for j
    """
    :param j: An optional parameter. Without a parameter the value '10' will be used.
    """
    output = sims4.commands.CheatOutput(_connection)
    try:
        logger(f"j: {type(j)} = i", output)  # Also logging type(j), which is 'str'. But the value may fail to convert to int (eg 0x1 fails)
        i = int(f"{j}")  # Converting str to int
        logger(f"{10/i:.2f}", output)
    except Exception as e:
        logger(f"Oops: {e}", output)
        logger(f"{traceback.format_exc()}", output)


@sims4.commands.Command('o19.tut.commands.5', command_type=sims4.commands.CommandType.Cheat)  # As .3, but 'CommandType.Cheat'
def o19_cheat_tut_commands_five(i: int = 10, _connection=None):
    """
    To use this command enter 'testingcheats true'. Disable it with 'testingcheats false' in the console.
    """
    output = sims4.commands.CheatOutput(_connection)
    try:
        logger(f"_connection: {type(_connection)} = _connection", output)
        logger(f"output: {type(output)} = output", output)
        logger(f"{10/i:.2f}", output)
    except Exception as e:
        logger(f"Oops: {e}", output)
        logger(f"{traceback.format_exc()}", output)
