import { PanelSectionRow, SliderField } from "decky-frontend-lib";
import { useState, VFC } from "react";

interface VolumeProps {
  sourceName: string
}

const VolumeControl: VFC<VolumeProps> = ({sourceName}: VolumeProps) => {
  /**
   * TODO: Remove this temporary state to use reducer approach
   */
  const [volumeValue, setVolumeValue] = useState(100)

  const volumeChangeHandler = (newVal: number) => {
    setVolumeValue(newVal)
  }

  return (
    <div>
      <div>
        {sourceName}
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