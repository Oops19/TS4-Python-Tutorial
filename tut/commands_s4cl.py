"""
Save this file in 'The Sims 4/Mods/_o19_/tut/' as 'commands_s4cl.py'
Enable custom content and script mods within TS4.

Once upon a time a man said: 'I bet it'd be even shorter if they used S4CL' - Let's proof this.
"""

# Import our classes
from tut.modinfo import ModInfo

# Import of S4CL classes
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry


log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity().name, ModInfo.get_identity().name)
log.enable()
log.debug(f"Starting {ModInfo.get_identity().name} v{ModInfo.get_identity().version}")  # log that we have been loaded


# CommonConsoleCommand(mod_identity, command_name, command_description, command_aliases=(), command_arguments=(),
#     command_type=CommandType.Live, command_restriction_flags=CommandRestrictionFlags.UNRESTRICTED,
#     required_pack_flags=None, console_type=None, show_with_help_command=True


@CommonConsoleCommand(ModInfo.get_identity(), 'o19.tut.commands.a', 'Run a console command.')
def o19_cheat_tut_commands_a(output: CommonConsoleCommandOutput, i: int):
    # output is already provided
    try:
        log.debug(f"{10 / i}")  # A custom logging method is no longer needed
        output(f"OK ('{10 / i:.2f}')")
    except Exception as e:
        log.error(f"Oops: {e}", throw=True)

'''
We expect that 'o19.tut.commands.a' silently fails as the required parameter is missing. But no, it displays:
"Missing some arguments ... 'ts4-tutorial.help o19.tut.commands.a' ..."  which we execute and it prints out:
"o19.tut.commands.a - Run a console command." - We will improve this:
'''


@CommonConsoleCommand(ModInfo.get_identity(), 'o19.tut.commands.b', 'The elite calculator to devide numbers.',
                      command_arguments=(
                              CommonConsoleCommandArgument('i', 'number', 'The divident.', is_optional=False),
                              CommonConsoleCommandArgument('j', 'number', 'The divisor.', is_optional=True, default_value='10'),
                      )
                      )
def o19_cheat_tut_commands_b(output: CommonConsoleCommandOutput, i: int, j: int = 10):
    try:
        log.debug(f"{j / i}")  # A custom logging method is no longer needed
        output(f"OK ('{j / i:.2f}')")
    except Exception as e:
        log.error(f"Oops: {e}", throw=True)

'''
We expect that 'o19.tut.commands.b' shows the similar error and it does
"Missing some arguments ... 'ts4-tutorial.help o19.tut.commands.b' ..." which we execute and it prints out:
"o19.tut.commands.b - The elite calculator to devide numbers.
i (number) - The divident.
[j=19] (number) - The divisor."

Nothing new for us, for users who use the mod only every 4 weeks it may be valuable information.
With 'ts4-tutorial.help' we get the both methods printed out, so it's easy to start as long as the (internal) mod name is known.
We can log it to the log file:
'''
log.debug(f"Enter '{ModInfo.get_identity().name.lower()}.help' in the console for help.")
