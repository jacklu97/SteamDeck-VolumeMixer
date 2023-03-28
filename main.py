# Special thanks to jurassicplayer.

import asyncio
import logging
import os
import subprocess
from typing import List

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
    
    async def mm_get_programs_names(self):
        logger.info('Getting a list of all running processes using audio interface')
        cmd = "pactl list sink-inputs"
        proc = await self.pyexec_subprocess(self, cmd)

        if (proc['returncode'] != 0):
            logging.info("There was an error on the excecution!")
            return []
        
        inputs = [line.strip() for line in proc['stdout'].splitlines() if 'application.name' in line]
        process_names = [input.split('"')[1] for input in inputs]

        return process_names

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
