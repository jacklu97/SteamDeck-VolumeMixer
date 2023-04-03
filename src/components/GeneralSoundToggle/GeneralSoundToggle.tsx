import { useEffect, useState } from "react";

import { PanelSection, PanelSectionRow, ToggleField } from "decky-frontend-lib";

import PythonServer from "../../services/pythonServer";

const GeneralSoundToggle = () => {
  const [isMuted, setIsMuted] = useState<boolean>(false)

  const server = PythonServer.getInstance()

  const handleToggle = () => {
    server.resolve(server.toggleMuteStatus(), () => setIsMuted(prev => !prev))
  }

  const getCurrentMuteStatus = (): Promise<MuteStatusResponse> => {
    return new Promise<MuteStatusResponse>((resolve) => {
      server.resolve(server.getMuteStatus(), (response: MuteStatusResponse) => {
        resolve(response)
      })
    })
  }

  useEffect(() => {
    getCurrentMuteStatus()
      .then(res => setIsMuted(res.isMuted))
  }, [])

  return (
    <PanelSection title="System Volume">
      <PanelSectionRow>
        <ToggleField
          label="Mute System"
          checked={isMuted}
          onChange={handleToggle}
        />
      </PanelSectionRow>
    </PanelSection>
  );
}

export default GeneralSoundToggle;