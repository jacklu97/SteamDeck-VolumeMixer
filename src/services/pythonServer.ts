import { ServerAPI, ServerResponse } from "decky-frontend-lib"

class PythonServer {
  private static instance: PythonServer
  private server: ServerAPI | undefined = undefined

  private constructor(){}

  static getInstance(): PythonServer {
    if(!PythonServer.instance) {
      PythonServer.instance = new PythonServer()
    }

    return PythonServer.instance
  }

  setServer(s: ServerAPI) {
    this.server = s;
  }

  getServer() {
    return this.server
  }

  resolve(promise: Promise<any>, setter: any) {
    (async function () {
      const data = await promise;
      if (data.success) {
        console.debug("Got resolved", data, "promise", promise);
        setter(data.result);
      } else {
        console.warn("Resolve failed:", data, "promise", promise);
      }
    })();
  }

  getPlayingProgramsNames(): Promise<any> {
    return this.server!.callPluginMethod('mm_get_programs_names', {})
  }

  setNewVolume(playerId: number, newVolumeVal: number): Promise<any> {
    return this.server!.callPluginMethod('mm_update_current_volume', {player_id: playerId, new_volume: newVolumeVal})
  }

}

export default PythonServer