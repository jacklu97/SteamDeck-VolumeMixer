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

### Making your own plugin

1. You can fork this repo or utilize the "Use this template" button on Github.
2. In your local fork/own plugin-repository run these commands:
   1. ``pnpm i``
   2. ``pnpm run build``
   - These setup pnpm and build the frontend code for testing.
3. Consult the [decky-frontend-lib](https://github.com/SteamDeckHomebrew/decky-frontend-lib) repository for ways to accomplish your tasks.
   - Documentation and examples are still rough, 
   - While decky-loader primarily targets Steam Deck hardware so keep this in mind when developing your plugin.
4. If you want an all encompassing demonstration of decky-frontend-lib's capabilities check out [decky-playground](https://github.com/SteamDeckHomebrew/decky-playground). It shows off almost all of decky-frontend-lib's features.

#### Other important information

Everytime you change the frontend code (`index.tsx` etc) you will need to rebuild using the commands from step 2 above or the build task if you're using vscode or a derivative.

Note: If you are receiving build errors due to an out of date library, you should run this command inside of your repository:

```bash
pnpm update decky-frontend-lib --latest
```

## Important information about privacy

This plugin doesn't use any root privileges to modify the volume level of the running applications nor sends any kind of data to the internet.