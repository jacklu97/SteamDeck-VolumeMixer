# Special thanks to jurassicplayer.

import asyncio
import json
import logging
import os
import re

from settings import SettingsManager # type: ignore
from helpers import get_user_id # type: ignore

# The decky plugin module is located at decky-loader/plugin
# For easy intellisense checkout the decky-loader code one directory up
# or add the `decky-loader/plugin` path to `python.analysis.extraPaths` in `.vscode/settings.json`
import decky_plugin

# Setup environment variables
deckyUserHome = os.environ["DECKY_USER_HOME"]
deckyHomeDir = os.environ["DECKY_HOME"]
settingsDir = os.environ["DECKY_PLUGIN_SETTINGS_DIR"]
loggingDir = os.environ["DECKY_PLUGIN_LOG_DIR"]
defaultAppDataDirectory = os.path.join(deckyUserHome, '.var', 'app')
XDG_RUNTIME_DIR = os.path.join(os.path.abspath(os.sep), 'run', 'user', str(get_user_id()))

# Setup backend logger
logging.basicConfig(filename=os.path.join(loggingDir, 'backend.log'),
                    format='[MusicMixer] %(asctime)s %(levelname)s %(message)s',
                    filemode='w+',
                    force=True)
logger=logging.getLogger()
logger.setLevel(logging.INFO) # can be changed to logging.DEBUG for debugging issues


class Plugin:
    async def pyexec_subprocess(self, cmd:str, input:str=''):
        logging.info(f'Calling python subprocess: "{cmd}"')
        runtimeDir = os.environ.get("XDG_RUNTIME_DIR")
        if not runtimeDir: runtimeDir = XDG_RUNTIME_DIR
        proc = await asyncio.create_subprocess_shell(cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.PIPE,
            env={"XDG_RUNTIME_DIR": runtimeDir})
        stdout, stderr = await proc.communicate(input.encode())
        stdout = stdout.decode()
        stderr = stderr.decode()
        logging.info(f'Returncode: {proc.returncode}\nSTDOUT: {stdout[:300]}\nSTDERR: {stderr[:300]}')
        return {'returncode': proc.returncode, 'stdout': stdout, 'stderr': stderr}
    
    async def extract_program_data(self, output: str):
        output_arr = []

        # Extract the sink input ID
        id_regex = r"Sink Input #(\d+)"
        ids = re.findall(id_regex, output)

        # Extract the application name
        app_regex = r"application.name = \"(.*?)\""
        apps = re.findall(app_regex, output, re.DOTALL)

        # Extract the volume percentage
        vol_regex = r"Volume:\s+.*?(\d+)%\s"
        volumes = re.findall(vol_regex, output, re.DOTALL)

        # Set the values into a dict
        for i in range(len(ids)):
            input = {
                'applicationId' : int(ids[i]),
                'applicationName' : apps[i],
                'currentVolume' : int(volumes[i])
            }
            output_arr.append(input)

        return output_arr
    
    async def mm_update_current_volume(self, player_id: str, new_volume: int):
        logger.info(f"Updating volume of app: {player_id} with value: {new_volume}")
        cmd = f"pactl set-sink-input-volume {player_id} {new_volume}%"
        proc = await self.pyexec_subprocess(self, cmd)

        if (proc['returncode'] != 0):
            logger.info(f"There was an error updating the volume of {player_id} to {new_volume}")
            return -1
        
    async def mm_get_programs_names(self):
        logger.info('Getting a list of all running processes using audio interface')
        cmd = "pactl list sink-inputs"
        proc = await self.pyexec_subprocess(self, cmd)

        if (proc['returncode'] != 0):
            logging.info("There was an error on the excecution!")
            return []
        
        process_names = await self.extract_program_data(self, proc['stdout'])
        logger.info(f"Returning to client: {process_names}")
        return process_names
    
    async def mm_toggle_mute_system(self):
        logger.info("Toggling mute state")
        cmd = "pactl set-sink-mute @DEFAULT_SINK@ toggle"
        proc = await self.pyexec_subprocess(self, cmd)

        if (proc['returncode'] != 0):
            logging.info("There was an error toggling the mute status")
            return -1
        
        return await self.mm_get_mute_status(self)
    
    async def mm_get_mute_status(self):
        logger.info("Getting current mute status")
        cmd = "pactl list sinks | grep -A 10 'State:.*RUNNING' | grep 'Mute:'"
        proc = await self.pyexec_subprocess(self, cmd)

        if (proc['returncode'] != 0):
            logger.info("There was an error getting the current status of mute")
            return -1
        
        # will get a 'no' or 'yes' from cmd
        try:
            is_muted = True if 'yes' == [i for i in re.sub(r'[\t\n]', '', proc["stdout"]).split("Mute: ")][-1] else False 
            response = {
                "isMuted" : is_muted
            }

            logger.info(f"Returning current mute state: {response}")
            return response
        except Exception as e:
            logger.info(f"There was an exception sending the response \n {e}")

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        decky_plugin.logger.info("Hello World!")

    # Function called first during the unload process, utilize this to handle your plugin being removed
    async def _unload(self):
        decky_plugin.logger.info("Goodbye World!")
        pass

    # Migrations that should be performed before entering `_main()`.
    async def _migration(self):
        decky_plugin.logger.info("Migrating")
        # Here's a migration example for logs:
        # - `~/.config/decky-template/template.log` will be migrated to `decky_plugin.DECKY_PLUGIN_LOG_DIR/template.log`
        decky_plugin.migrate_logs(os.path.join(decky_plugin.DECKY_USER_HOME,
                                               ".config", "decky-template", "template.log"))
        # Here's a migration example for settings:
        # - `~/homebrew/settings/template.json` is migrated to `decky_plugin.DECKY_PLUGIN_SETTINGS_DIR/template.json`
        # - `~/.config/decky-template/` all files and directories under this root are migrated to `decky_plugin.DECKY_PLUGIN_SETTINGS_DIR/`
        decky_plugin.migrate_settings(
            os.path.join(decky_plugin.DECKY_HOME, "settings", "template.json"),
            os.path.join(decky_plugin.DECKY_USER_HOME, ".config", "decky-template"))
        # Here's a migration example for runtime data:
        # - `~/homebrew/template/` all files and directories under this root are migrated to `decky_plugin.DECKY_PLUGIN_RUNTIME_DIR/`
        # - `~/.local/share/decky-template/` all files and directories under this root are migrated to `decky_plugin.DECKY_PLUGIN_RUNTIME_DIR/`
        decky_plugin.migrate_runtime(
            os.path.join(decky_plugin.DECKY_HOME, "template"),
            os.path.join(decky_plugin.DECKY_USER_HOME, ".local", "share", "decky-template"))
