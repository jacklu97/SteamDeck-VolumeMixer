import { ReactElement, useEffect, useState } from "react";

import { PanelSection, Spinner } from "decky-frontend-lib";

import PythonServer from "../../services/pythonServer";
import VolumeControl from "../UI/VolumeControl";
import EmptySources from "./EmptySources";

const AvailableSources = () => {
  const [programs, setPrograms]: [Array<Player>, Function] = useState([])

  const getPrograms = () => {
    const server = PythonServer.getInstance()

    server.resolve(server.getPlayingProgramsNames(), (players: Array<Player>) => {
      setPrograms(players)
    })

  }

  useEffect(() => {
    getPrograms()
  }, [])

  let content: ReactElement<any, any>[] | ReactElement<any, any> = <Spinner />

  if (programs.length > 0) {
    content = programs.map(p =>
      <VolumeControl
        key={p.applicationId}
        sourceName={p.applicationName}
        currentVolume={p.currentVolume}
        sourceId={p.applicationId}
      />
    )
  } else {
    content = <EmptySources />
  }

  return (
    <PanelSection title="List of applications">
      {content}
    </PanelSection>
  );
}

export default AvailableSources;