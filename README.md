# Steam Deck Volume Mixer plugin

A [decky-loader](https://github.com/SteamDeckHomebrew/decky-loader) plugin that allows the user to control the volume of any running program on the steam deck individually. Inspired on the functionality of Windows' Volume Mixer.

## Dependencies

This plugin was created using the [decky-plugin-template](https://github.com/SteamDeckHomebrew/decky-plugin-template) and uses its dependencies. 

Relies on the user having `pnpm` installed on their system. This can be downloaded from `npm` itself which is recommended. 

#### Linux

```bash
sudo npm i -g pnpm
```

### How to run

Clone this repo and run these commands:

```bash
pnpm i
pnpm run build
```

To transfer this plugin to the deck you can run the vscode tasks that are configured to deploy it to your deck, checkout .vscode folder for reference.

#### Other important information

Everytime you change the frontend code (`index.tsx` etc) you will need to rebuild using the commands from step 2 above or the build task if you're using vscode or a derivative.

Note: If you are receiving build errors due to an out of date library, you should run this command inside of your repository:

```bash
pnpm update decky-frontend-lib --latest
```

## Important information about privacy

This plugin doesn't use any root privileges to modify the volume level of the running applications nor sends any kind of data to the internet.