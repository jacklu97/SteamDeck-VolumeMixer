import { PanelSectionRow, SliderField } from "decky-frontend-lib";
import { useState, VFC } from "react";
import PythonServer from "../../services/pythonServer";

interface VolumeProps {
  sourceId: number
  sourceName: string
  currentVolume: number
}

const VolumeControl: VFC<VolumeProps> = ({sourceName, currentVolume, sourceId}: VolumeProps) => {
  /**
   * TODO: Remove this temporary state to use reducer approach
   */
  const [volumeValue, setVolumeValue] = useState(currentVolume)

  const fixedSourceName = sourceName.charAt(0).toUpperCase() + sourceName.slice(1)

  const volumeChangeHandler = (newVal: number) => {
    setVolumeValue(newVal)
    
    const server = PythonServer.getInstance()
    
    server.resolve(server.setNewVolume(sourceId, newVal), () => {
      
    })
  }

  return (
    <div>
      <div>
        {fixedSourceName}
      </div>
      <PanelSectionRow>
        <SliderField
          value={volumeValue}
          min={0}
          max={100}
          step={1}
          onChange={volumeChangeHandler}
        />
      </PanelSectionRow>
    </div>
  );
}

export default VolumeControl;