import { Spinner } from "decky-frontend-lib";
import { ReactElement, useEffect, useState } from "react";
import { useQuery } from "react-query";
import PythonServer from "../../services/pythonServer";
import VolumeControl from "../UI/VolumeControl";
import EmptySources from "./EmptySources";

const AvailableSources = () => {
  const [programs, setPrograms]: [Array<string>, Function] = useState([])

  const getPrograms = () => {
    const server = PythonServer.getInstance()

    server.resolve(server.getPlayingProgramsNames(), (players: Array<string>) => {
      setPrograms(players)
    })

  }

  // const { isLoading, isError, data, error } = useQuery('getPrograms', 
  //   PythonServer.getInstance().getPlayingProgramsNames, 
  //   {staleTime: 60 * 500}
  // )

  useEffect(() => {
    getPrograms()
  }, [])

  let content: ReactElement<any, any>[] | ReactElement<any, any> = <Spinner />

  if (programs.length > 0) {
    content = programs.map(p => <VolumeControl sourceName={p} />)
  } else {
    content = <EmptySources />
  }

  return ( 
    <div>
      {content}
    </div>
   );
}
 
export default AvailableSources;