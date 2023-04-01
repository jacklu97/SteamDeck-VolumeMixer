import { PanelSectionRow, SliderField } from "decky-frontend-lib";
import { useState, VFC } from "react";

interface VolumeProps {
  sourceName: string
  currentVolume: number
}

const VolumeControl: VFC<VolumeProps> = ({sourceName, currentVolume}: VolumeProps) => {
  /**
   * TODO: Remove this temporary state to use reducer approach
   */
  const [volumeValue, setVolumeValue] = useState(currentVolume)

  const fixedSourceName = sourceName.charAt(0).toUpperCase() + sourceName.slice(1)

  const volumeChangeHandler = (newVal: number) => {
    setVolumeValue(newVal)
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