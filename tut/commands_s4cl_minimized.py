from tut.modinfo import ModInfo
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity().name, ModInfo.get_identity().name)
log.enable()
@CommonConsoleCommand(ModInfo.get_identity(), 'o19.tut.commands.a_min', 'Run a console command.')
def o19_cheat_tut_commands_a_min(output: CommonConsoleCommandOutput, i: int):
    try:
        log.debug(f"10/{i} = '{10/i:3.2f}'")
    except Exception as e:
        log.error(f"Oops: {e}", throw=True)
# Down to 12 lines
